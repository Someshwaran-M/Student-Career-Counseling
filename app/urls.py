from django.urls import path
from . import views

urlpatterns = [
    path('', views.temheader, name="temheader"),
	path('register/', views.register,name="register"),
	path('login/', views.student_login,name="student_login"),
	path('dashboard/', views.dashboard,name="dashboard"),
	path('logout/', views.logout,name="logout"),
	path('choose_college/', views.choose_college,name="choose_college"),
	path('college_login/', views.college_login,name="college_login"),
	path('college_dashboard/', views.college_dashboard,name="college_dashboard"),
	path('college_logout/', views.college_logout,name="college_logout"),
	path('add_question/', views.add_question,name="add_question"),
	path('question/<int:pk>/', views.question,name="question"),
	path('category_detail/', views.category_detail,name="category_detail"),
	path('delete/<int:pk>/', views.delete,name="delete"),
	path('apply_course/<int:pk>/', views.apply_course,name="apply_course"),
	path('applied_students/', views.applied_students,name="applied_students"),
	path('update_status/<int:pk>/', views.update_status,name="update_status"),
	path('allocated_test/', views.allocated_test,name="allocated_test"),
	path('applied_details/', views.applied_details,name="applied_details"),
	path('exam/<int:pk>/<int:col_id>/', views.exam,name="exam"),
	path('result/', views.result,name="result"),
	path('view_exam/', views.view_exam,name="view_exam"),
	path('exam_result/<int:cat_id>/', views.exam_result,name="exam_result"),
	path('college_result/<int:cat_id>/<int:pk>/', views.college_result,name="college_result"),
	path('sheet_status/<int:pk>/', views.sheet_status,name="sheet_status"),
	path('student_sheet_status/<int:pk>/', views.student_sheet_status,name="student_sheet_status"),
	path('admin_exam/', views.admin_exam,name="admin_exam"),
	path('admin_student_result/<int:cat_id>/<int:pk>/', views.admin_student_result,name="admin_student_result"),
	path('admin_exam_publish/<int:cat_id>/<int:pk>/', views.admin_exam_publish,name="admin_exam_publish"),

]
