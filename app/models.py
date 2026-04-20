from django.db import models


class College_Detail(models.Model):
	college_name = models.CharField('College Name',max_length=100)
	email = models.EmailField('Email Id',max_length=100)
	mobile = models.CharField('Mobile Num',max_length=30)
	accommodation_fee = models.CharField('Accommodation Fee',max_length=300)
	eligibility = models.CharField('Eligibility',max_length=300)
	placement = models.TextField('Placement Opportunity',max_length=2000)
	scholarship_scheme = models.TextField('Scholarship Scheme',max_length=2000)
	rules = models.TextField('Rules and Regulations',max_length=2000)
	image = models.FileField('College Image',upload_to='product/',null=True)
	course = models.TextField('Course',max_length=3000)
	username = models.CharField('Username',max_length=100,null=True)
	password = models.CharField('Password',max_length=100,null=True)
	country = models.CharField('Country',max_length=100)
	city = models.CharField(' City',max_length=300)
	address = models.TextField(' Address',max_length=2000)
	notes = models.TextField('Notes',max_length=3000)
def __str__(self):
        return self.college_name
class Student_Detail(models.Model):
	student_name = models.CharField('Student Name', max_length=255)
	email_id = models.EmailField('Email Id', max_length=255)
	phone_number = models.CharField('Mobile Number', max_length=50,null=True,blank=True)
	dob =  models.DateField()
	gender = models.CharField('Gender',max_length=20)
	education = models.CharField('Education',max_length=200)
	Score = models.CharField('Score',max_length=200)
	address = models.TextField('Address',null=True,blank=True)
	country = models.CharField('Country', max_length=100,default='India')
	state = models.CharField('State', max_length=100,default='Tamil Nadu')
	city = models.CharField('City', max_length=100,null=True,blank=True)
	username = models.CharField('Username', max_length=100, unique=True)
	password = models.CharField('Password',max_length=30)
	image = models.FileField('Student Image',upload_to='documents/',null=True)
	def __str__(self):
		return self.student_name
class Question_Category(models.Model):
	name = models.CharField('Category Name', max_length=255)
	def __str__(self):
		return self.name
class Quiz_Question(models.Model):
	category = models.ForeignKey(Question_Category, on_delete=models.CASCADE,null=True)
	college = models.ForeignKey(College_Detail, on_delete=models.CASCADE,null=True)
	question = models.CharField('Question', max_length=255)
	option1 = models.CharField('Option1', max_length=255)
	option2 = models.CharField('Option2', max_length=255)
	option3 = models.CharField('Option3', max_length=255)
	option4 = models.CharField('Option4', max_length=255)
	answer = models.CharField('Answer', max_length=255)
	def __str__(self):
		return self.question

STS = (
    ('','Select'),
    ('pending','Pending'),
    ('publish','Publish'),
)

STATU = (
    ('','Select'),
    ('test','Take Test'),
    ('rejected','Rejected'),
)
TEST = (
    ('','Select'),
    ('taken','Test Taken'),
    ('not','Not Yet'),
)
class Answer_Detail(models.Model):
	question = models.IntegerField(null=True)
	college_id = models.ForeignKey(College_Detail, on_delete=models.CASCADE,null=True)
	rand_num = models.CharField(max_length=255)
	ans = models.CharField('Answer', max_length=255)
	user_id = models.ForeignKey(Student_Detail, on_delete=models.CASCADE)
	category_id = models.ForeignKey(Question_Category, on_delete=models.CASCADE,null=True)
	status = models.CharField('Publish Answer',max_length=30,choices=STS,null=True)
	def __str__(self):
		return self.ans

class Apply(models.Model):
	student_id = models.ForeignKey(Student_Detail, on_delete=models.CASCADE,null=True)
	college_id = models.ForeignKey(College_Detail, on_delete=models.CASCADE,null=True)
	course = models.CharField(max_length=255)
	mark = models.CharField('12th Mark', max_length=255)
	certificate = models.FileField('Upload Certificate',upload_to='documents/')
	aadhaar = models.CharField(max_length=50,null=True,blank=True)
	community = models.CharField(max_length=255)
	commun = models.FileField('Upload Community',upload_to='documents/',null=True)
	proof = models.FileField('Upload Aadhaar',upload_to='documents/',null=True)
	category_id = models.ForeignKey(Question_Category, on_delete=models.CASCADE,null=True,blank=True)
	status = models.CharField('Status',max_length=30,choices=STATU,null=True,blank=True)
	test_status = models.CharField('Test Status',max_length=30,choices=TEST,null=True,blank=True)
	sheet = models.CharField('Sheet Confirmed',max_length=30,null=True,blank=True)
	amount = models.CharField('Amount',max_length=30,null=True,blank=True)
	documents = models.TextField('Document Should Carry',max_length=3000,null=True,blank=True)
	date = models.DateField('Date',null=True,blank=True)

	def __str__(self):
		return self.student_id.student_name
