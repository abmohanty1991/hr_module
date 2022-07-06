from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib.auth import logout, authenticate, login
from .models import *
from django.contrib import messages
# from passlib.hash import pbkdf2_sha256
from .models import *
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.views.decorators.cache import cache_control,never_cache
# from django.views.decorators.cache import never_cache


def home(request):
	return render(request, 'home.html')


def contact(request):
	return render(request, 'contact.html')


# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def loginUser(request):
	return render(request, 'login_page.html')


# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def doLogin(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	if not (username and password):
		messages.error(request, "Please provide all the details!!")
		return render(request, 'login_page.html')
	
	user = authenticate(username=username,password=password)
	
	if user is not None:
		login(request,user)
		return render (request,'hod_template/home_content.html' )
	else:
		print("abcd")
		messages.error(request,"Invalid credentials")
		return render(request, 'login_page.html')

	# password_db = User.objects.filter(username=pno).values("password").last()
	# pass_check = pbkdf2_sha256.verify(password,password_db["password"])
	# if  pass_check == False:
	# 	messages.error(request, 'Invalid Login Credentials!!')
	# 	return render(request, 'login_page.html')
	# elif pass_check == True:
	# 	return render(request,'hod_template/home_content.html')

	# if user.user_type == HrmUsers.STUDENT:
	# 	return redirect('student_home/')
	# elif user.user_type == HrmUsers.STAFF:
	# 	return redirect('staff_home/')
	# elif user.user_type == HrmUsers.HOD:
	# 	return redirect('admin_home/')

	return render(request, 'admin_home.html')


def registration(request):
	return render(request, 'registration.html')


def doRegistration(request):
	first_name = request.POST.get('first_name')
	last_name = request.POST.get('last_name')
	username = request.POST.get('username')
	raw_password = request.POST.get('password')
	confirm_password = request.POST.get('confirmPassword')

	print(username)
	print(raw_password)
	print(confirm_password)
	print(first_name)
	print(last_name)
	if not (username and raw_password and confirm_password):
		messages.error(request, 'Please provide all the details!!')
		return render(request, 'registration.html')

	if raw_password != confirm_password:
		messages.error(request, 'Both passwords should match!!')
		return render(request, 'registration.html')

	# user_type = get_user_type_from_email(email_id)

	# if user_type is None:
	# 	messages.error(
	# 		request, "Please use valid format for the email id: '<username>.<staff|student|hod>@<college_domain>'")
	# 	return render(request, 'registration.html')

	# if HmUsers.objects.filter(username=username).exists():
	# 	messages.error(
	# 		request, 'User with this username already exists. Please use different username')
	# 	return render(request, 'registration.html')

	# user = HrmUsers()
	# user.username = username
	# user.pno = username
	# # user.email = email_id
	# user.password = raw_password
	# # user.user_type = user_type
	# user.first_name = first_name
	# user.last_name = last_name
	user = HrmUsers.objects.create_user(username=username, password=raw_password,pno=username,first_name=first_name,last_name=last_name)
	# user.save()

	# if user_type == HrmUsers.STAFF:
	# 	Staffs.objects.create(admin=user)
	# elif user_type == HrmUsers.STUDENT:
	# 	Students.objects.create(admin=user)
	# elif user_type == HrmUsers.HOD:
	# 	AdminHOD.objects.create(admin=user)
	return render(request, 'login_page.html')
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	# first_name = request.GET.get('first_name')
	# last_name = request.GET.get('last_name')
	# pno = request.GET.get('pno')
	# password = request.GET.get('password')
	# confirm_password = request.GET.get('confirmPassword')

	# if not (pno and password and confirm_password):
	# 	messages.error(request, 'Please provide all the details!!')
	# 	return render(request, 'registration.html')

	# if password != confirm_password:
	# 	messages.error(request, 'Both passwords should match!!')
	# 	return render(request, 'registration.html')

	# is_user_exists = HrmUsers.objects.filter(pno=pno).exists()

	# if is_user_exists:
	# 	messages.error(
	# 		request, 'User with this pno already exists. Please proceed to login!!')
	# 	return render(request, 'registration.html')

	# user_type = get_user_type_from_email(email_id)

	# if user_type is None:
	# 	messages.error(
	# 		request, "Please use valid format for the email id: '<username>.<staff|student|hod>@<college_domain>'")
	# 	return render(request, 'registration.html')

	# username = email_id.split('@')[0].split('.')[0]

	# if HrmUsers.objects.filter(username=username).exists():
	# 	messages.error(
	# 		request, 'User with this username already exists. Please use different username')
	# 	return render(request, 'registration.html')

	# enc_password = pbkdf2_sha256.encrypt(password.encode('utf-8'),rounds=12000,salt_size = 32)
	# user = HrmUsers()
	# user.pno = pno
	# # user.email = email_id
	# user.password = enc_password
	# # user.user_type = user_type
	# user.first_name = first_name
	# user.last_name = last_name
	# user.save()

	# # if user_type == HrmUsers.STAFF:
	# # 	Staffs.objects.create(admin=user)
	# # elif user_type == HrmUsers.STUDENT:
	# # 	Students.objects.create(admin=user)
	# # elif user_type == HrmUsers.HOD:
	# # 	AdminHOD.objects.create(admin=user)
	# return render(request, 'login_page.html')

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout_user(request):
	logout(request)
	return HttpResponseRedirect('/')


# def get_user_type_from_email(email_id):
# 	"""
# 	Returns HrmUsers.user_type corresponding to the given email address
# 	email_id should be in following format:
# 	'<username>.<staff|student|hod>@<college_domain>'
# 	eg.: 'abhishek.staff@jecrc.com'
# 	"""

# 	try:
# 		email_id = email_id.split('@')[0]
# 		email_user_type = email_id.split('.')[1]
# 		return HrmUsers.EMAIL_TO_USER_TYPE_MAP[email_user_type]
# 	except:
# 		return None

# Create your views here.
