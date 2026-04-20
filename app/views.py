from django.shortcuts import render,redirect
from django.contrib import messages
from . models import *
import random 
from django.db.models import Sum, Count
from django.db import connection
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from . performance import *
import random 

def student_login(request):
	if request.session.has_key('user_id'):
		return render(request,'dashboard.html',{})
	else:
		if request.method == 'POST':
			name=request.POST.get('username')
			pwd=request.POST.get('password')
			user_exist=Student_Detail.objects.filter(username=name,password=pwd)
			if user_exist:
				request.session['name']= request.POST.get('username')
				a = request.session['name']
				sess = Student_Detail.objects.only('id').get(username=a).id
				request.session['user_id']= sess
				return redirect('dashboard')
			else:
				messages.success(request,'Invalid username or Password')
		return render(request,'student_login.html',{})
def dashboard(request):
	if request.session.has_key('user_id'):
		return render(request,'dashboard.html',{})
	else:
		return render(request,'student_login.html',{})
def register(request):
	if request.method == 'POST':
		Name = request.POST.get('uname')
		Adddress = request.POST.get('address')
		Mobile= request.POST.get('mobile')
		Email = request.POST.get('email')
		Password = request.POST.get('pwd')
		unum = request.POST.get('username')
		country = request.POST.get('country')
		city = request.POST.get('city')
		state = request.POST.get('state')
		dob = request.POST.get('dob')
		gender = request.POST.get('gender')
		education = request.POST.get('education')
		score = request.POST.get('score')
		image = request.FILES['image']
		student_exist = Student_Detail.objects.filter(username=unum)
		if student_exist:
			messages.success(request,'Username No Already Exsit')
		else:
			crt = Student_Detail.objects.create(student_name=Name,
			address=Adddress,phone_number=Mobile,password=Password,email_id=Email,username=unum,country=country,
			city=city,state=state,dob=dob,gender=gender,education=education,Score=score,image=image)
			if crt:
				messages.success(request,'Registered Successfully')
	return render(request,'register.html',{})
def logout(request):
    try:
        del request.session['user_id']
        del request.session['name']
    except:
     pass
    return render(request, 'student_login.html', {})
def choose_college(request):
	if request.session.has_key('user_id'):
		a = College_Detail.objects.all()
		return render(request,'choose_college.html',{'a':a})
	else:
		return render(request,'student_login.html',{})
def college_login(request):
	if request.session.has_key('college_id'):
		return render(request,'college_dashboard.html',{})
	else:
		if request.method == 'POST':
			name=request.POST.get('username')
			pwd=request.POST.get('password')
			user_exist=College_Detail.objects.filter(username=name,password=pwd)
			if user_exist:
				request.session['college']= request.POST.get('username')
				a = request.session['college']
				sess = College_Detail.objects.only('id').get(username=a).id
				request.session['college_id']= sess
				return redirect('college_dashboard')
			else:
				messages.success(request,'Invalid username or Password')
		return render(request,'college_login.html',{})
def college_dashboard(request):
	if request.session.has_key('college_id'):
		return render(request,'college_dashboard.html',{})
	else:
		return render(request,'college_login.html',{})
def college_logout(request):
    try:
        del request.session['college_id']
        del request.session['college']
    except:
     pass
    return render(request, 'college_login.html', {})
def add_question(request):
	if request.session.has_key('college_id'):
		user_id = request.session['college_id']
		detail = Question_Category.objects.all()
		if request.method == 'POST':
			category = request.POST.get('category')
			question = request.POST.get('question')
			option1 = request.POST.get('option1')
			option2 = request.POST.get('option2')
			option3 = request.POST.get('option3')
			option4 = request.POST.get('option4')
			answer = request.POST.get('answer')
			category_id = Question_Category.objects.get(id=int(category))
			college_id = College_Detail.objects.get(id=int(user_id))
			crt = Quiz_Question.objects.create(category=category_id,question=question,option1=option1,option2=option2,
			option3=option3,option4=option4,college=college_id,answer=answer)
			if crt:
				messages.success(request,'Question Added Successfully.')
		return render(request,'add_question.html',{'detail':detail})
	else:
		return render(request,'college_login.html',{})
def question(request,pk):
	if request.session.has_key('college_id'):
		user_id = request.session['college_id']
		detail = Quiz_Question.objects.filter(college=int(user_id),category=pk)
		return render(request,'questions.html',{'detail':detail})
	else:
		return render(request,'college_login.html',{})
def category_detail(request):
	if request.session.has_key('college_id'):
		detail = Question_Category.objects.all()
		return render(request,'category_detail.html',{'detail':detail})
	else:
		return render(request,'college_login.html',{})
def delete(request,pk):
	if request.session.has_key('college_id'):
		detail = Quiz_Question.objects.filter(id=pk).delete()
		return redirect('category_detail')
	else:
		return render(request,'college_login.html',{})
def apply_course(request,pk):
	if request.session.has_key('user_id'):
		user_id = request.session['user_id']
		if request.method == 'POST':
			course = request.POST.get('course')
			mark = request.POST.get('mark')
			certificate = request.FILES['certificate']
			aadhaar = request.POST.get('aadhaar')
			proof = request.FILES['proof']
			community = request.POST.get('community')
			commun = request.FILES['commun']
			student_id = Student_Detail.objects.get(id=int(user_id))
			college_id = College_Detail.objects.get(id=pk)
			crt = Apply.objects.create(course=course,mark=mark,certificate=certificate,aadhaar=aadhaar,proof=proof,
			community=community,commun=commun,student_id=student_id,college_id=college_id)
			if crt:
				messages.success(request,'We Will Update You Soon.')
		return render(request,'apply_course.html',{})
	else:
		return render(request,'student_login.html',{})
def applied_students(request):
	if request.session.has_key('college_id'):
		user_id = request.session['college_id']
		detail = Apply.objects.filter(college_id=int(user_id))
		return render(request,'applied_students.html',{'detail':detail})
	else:
		return render(request,'college_login.html',{})
def update_status(request,pk):
	if request.session.has_key('college_id'):
		user_id = request.session['college_id']
		detail = Question_Category.objects.all()
		if request.method == 'POST':
			a = request.POST.get('category')
			b = request.POST.get('status')
			c = request.POST.get('test_status')
			category = Question_Category.objects.get(id=int(a))
			crt = Apply.objects.filter(id=pk).update(category_id=category,status=b,test_status=c)
			if crt:
				messages.success(request,'Updated Successfully.')
		return render(request,'update_status.html',{'detail':detail})
def allocated_test(request):
	if request.session.has_key('college_id'):
		user_id = request.session['college_id']
		detail = Apply.objects.filter(status='test',college_id=int(user_id))
		return render(request,'allocated_test.html',{'detail':detail})
	else:
		return render(request,'college_login.html',{})
def applied_details(request):
	if request.session.has_key('user_id'):
		user_id = request.session['user_id']
		detail = Apply.objects.filter(student_id=int(user_id))
		return render(request,'applied_details.html',{'detail':detail})
	else:
		return render(request,'student_login.html',{})
def exam(request,pk,col_id):
	if request.session.has_key('user_id'):
		user_id = request.session['user_id']
		category_name = Question_Category.objects.filter(id=pk)
		detail = Quiz_Question.objects.filter(college=col_id,category=pk)
		student_id = Student_Detail.objects.get(id=int(user_id))
		category_id = Question_Category.objects.get(id=pk)
		college_id = College_Detail.objects.get(id=col_id)
		r_num =  random.randrange(20, 50, 3)
		num = r_num+pk
		if request.method == 'POST':
			Apply.objects.filter(student_id=int(user_id),category_id=pk).update(test_status='taken')
			question_id = request.POST.getlist('question_id')
			ran_num = request.POST.get('random_num')
			ans = request.POST.getlist('answer')
			length = len(ans)
			for i in range(0,length):
				crt = Answer_Detail.objects.create(question=int(question_id[i]),rand_num=ran_num,ans=ans[i],
				user_id=student_id,category_id=category_id,college_id=college_id,status='pending')
			if crt:
				return redirect('result')
		return render(request,'exam.html',{'detail':detail,'category_name':category_name,'num':num})
	else:
		return render(request,'student_login.html',{})
def result(request):
	if request.session.has_key('user_id'):
		return render(request,'result.html',{})
	else:
		return render(request,'student_login.html',{})
def view_exam(request):
	if request.session.has_key('user_id'):
		user_id = request.session['user_id']
		detail = Apply.objects.filter(student_id=int(user_id),status='test',test_status='taken')
		return render(request,'view_exam.html',{'detail':detail})
	else:
		return render(request,'student_login.html',{})
def exam_result(request,cat_id):
	if request.session.has_key('user_id'):
		user_id = request.session['user_id']
		cursor = connection.cursor()
		tt = cursor.execute('''SELECT app_answer_detail.rand_num from app_answer_detail where 
		app_answer_detail.user_id_id= '%d' AND app_answer_detail.category_id_id= '%d' ''' % (int(user_id),cat_id))
		row_user = cursor.fetchone()		
		cat_name = Answer_Detail.objects.filter(rand_num=row_user[0])
		sql = ''' SELECT COUNT(a.ans),a.status from app_quiz_question as q INNER JOIN app_answer_detail as a ON
		q.answer=a.ans where a.rand_num='%s' AND a.user_id_id= '%d' AND a.status='publish' ''' % (row_user[0],int(user_id))
		post = cursor.execute(sql)
		row = cursor.fetchall()
		
		return render(request,'exam_result.html',{'row':row,'cat_name':cat_name})
	else:
		return render(request,'student_login.html',{})
def college_result(request,cat_id,pk):
	if request.session.has_key('college_id'):
		user_id = request.session['college_id']
		cursor = connection.cursor()
		tt = cursor.execute('''SELECT app_answer_detail.rand_num from app_answer_detail where 
		app_answer_detail.user_id_id= '%d' AND app_answer_detail.category_id_id= '%d' ''' % (pk,cat_id))
		row_user = cursor.fetchone()		
		cat_name = Answer_Detail.objects.filter(rand_num=row_user[0])
		sql = ''' SELECT COUNT(a.ans),a.status from app_quiz_question as q INNER JOIN app_answer_detail as a ON
		q.answer=a.ans where a.rand_num='%s' AND a.user_id_id= '%d' AND a.status='publish' ''' % (row_user[0],pk)
		post = cursor.execute(sql)
		row = cursor.fetchall()
		return render(request,'college_result.html',{'row':row,'cat_name':cat_name})
	else:
		return render(request,'college_login.html',{})
def sheet_status(request,pk):
	if request.session.has_key('college_id'):
		user_id = request.session['college_id']
		detail = Apply.objects.filter(id=pk)
		if request.method == 'POST':
			sheet = request.POST.get('sheet')
			amount = request.POST.get('amount')
			documents = request.POST.get('documents')
			date = request.POST.get('date')
			upd = Apply.objects.filter(id=pk).update(sheet=sheet,amount=amount,documents=documents,date=date)
			if upd:
				return redirect('allocated_test')
		return render(request,'sheet_status.html',{'detail':detail})
	else:
		return render(request,'college_login.html',{})
def student_sheet_status(request,pk):
	if request.session.has_key('user_id'):
		user_id = request.session['user_id']
		detail = Apply.objects.filter(id=pk)
		return render(request,'student_sheet_status.html',{'detail':detail})
	else:
		return render(request,'student_login.html',{})
def admin_exam(request):
	detail = Apply.objects.filter(test_status='taken')
	return render(request,'admin_result.html',{'detail':detail})
def admin_student_result(request,cat_id,pk):
	cursor = connection.cursor()
	tt = cursor.execute('''SELECT app_answer_detail.rand_num from app_answer_detail where 
	app_answer_detail.user_id_id= '%d' AND app_answer_detail.category_id_id= '%d' ''' % (pk,cat_id))
	row_user = cursor.fetchone()		
	cat_name = Answer_Detail.objects.filter(rand_num=row_user[0])
	sql = ''' SELECT COUNT(a.ans),a.status from app_quiz_question as q INNER JOIN app_answer_detail as a ON
	q.answer=a.ans where a.rand_num='%s' AND a.user_id_id= '%d' ''' % (row_user[0],pk)
	post = cursor.execute(sql)
	row = cursor.fetchall()
	return render(request,'admin_student_result.html',{'row':row,'cat_name':cat_name,'cat_id':cat_id,'pk':pk})
def admin_exam_publish(request,cat_id,pk):
	Answer_Detail.objects.filter(user_id=pk,category_id=cat_id).update(status='publish')
	detail = Apply.objects.filter(test_status='taken')
	return render(request,'admin_exam_publish.html',{'detail':detail})
def temheader(request):
    return render(request, "temheader.html", {})
