from datetime import datetime
from xmlrpc.client import TRANSPORT_ERROR
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.decorators import login_required
from pydoc import doc
from django.views.decorators.cache import cache_control

# from .forms import AddStudentForm, EditStudentForm

from .models import *
from django.views.decorators.cache import cache_control
from .filters import *


# `@login_required(login_url=LOGIN_REDIRECT_URL)`

LOGIN_REDIRECT_URL = 'login'

#####@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url=LOGIN_REDIRECT_URL)
def admin_home(request):

    # all_student_count = Students.objects.all().count()
    # subject_count = Subjects.objects.all().count()
    # course_count = Courses.objects.all().count()
    # staff_count = Staffs.objects.all().count()
    # course_all = Courses.objects.all()
    course_name_list = []
    subject_count_list = []
    student_count_list_in_course = []

    # for course in course_all:
    #     subjects = Subjects.objects.filter(course_id=course.id).count()
    #     students = Students.objects.filter(course_id=course.id).count()
    #     course_name_list.append(course.course_name)
    #     subject_count_list.append(subjects)
    #     student_count_list_in_course.append(students)

    # subject_all = Subjects.objects.all()
    subject_list = []
    student_count_list_in_subject = []
    # for subject in subject_all:
    #     course = Courses.objects.get(id=subject.course_id.id)
    #     student_count = Students.objects.filter(course_id=course.id).count()
    #     subject_list.append(subject.subject_name)
    #     student_count_list_in_subject.append(student_count)

    # # For Saffs
    staff_attendance_present_list = []
    staff_attendance_leave_list = []
    staff_name_list = []

    # staffs = Staffs.objects.all()
    # for staff in staffs:
    #     subject_ids = Subjects.objects.filter(staff_id=staff.admin.id)
    #     attendance = Attendance.objects.filter(
    #         subject_id__in=subject_ids).count()
    #     leaves = LeaveReportStaff.objects.filter(staff_id=staff.id,
    #                                              leave_status=1).count()
    #     staff_attendance_present_list.append(attendance)
    #     staff_attendance_leave_list.append(leaves)
    #     staff_name_list.append(staff.admin.first_name)

    # For Students
    student_attendance_present_list = []
    student_attendance_leave_list = []
    student_name_list = []

    # students = Students.objects.all()
    # for student in students:
    #     attendance = AttendanceReport.objects.filter(student_id=student.id,
    #                                                  status=True).count()
    #     absent = AttendanceReport.objects.filter(student_id=student.id,
    #                                              status=False).count()
    #     leaves = LeaveReportStudent.objects.filter(student_id=student.id,
    #                                                leave_status=1).count()
    #     student_attendance_present_list.append(attendance)
    #     student_attendance_leave_list.append(leaves+absent)
    #     student_name_list.append(student.admin.first_name)
        

    context = {
        # "all_student_count": all_student_count,
        # "subject_count": subject_count,
        # "course_count": course_count,
        # "staff_count": staff_count,
        # "course_name_list": course_name_list,
        # "subject_count_list": subject_count_list,
        # "student_count_list_in_course": student_count_list_in_course,
        # "subject_list": subject_list,
        # "student_count_list_in_subject": student_count_list_in_subject,
        # "staff_attendance_present_list": staff_attendance_present_list,
        # "staff_attendance_leave_list": staff_attendance_leave_list,
        # "staff_name_list": staff_name_list,
        # "student_attendance_present_list": student_attendance_present_list,
        # "student_attendance_leave_list": student_attendance_leave_list,
        # "student_name_list": student_name_list,
        "all_student_count": 0,
        "subject_count": 0,
        "course_count": 0,
        "staff_count": 0,
        "course_name_list": [],
        "subject_count_list": [],
        "student_count_list_in_course": [],
        "subject_list": [],
        "student_count_list_in_subject": [],
        "staff_attendance_present_list": [],
        "staff_attendance_leave_list": [],
        "staff_name_list": [],
        "student_attendance_present_list": [],
        "student_attendance_leave_list": [],
        "student_name_list": [],
    }
    return render(request, "hod_template/home_content.html", context)



@login_required(login_url=LOGIN_REDIRECT_URL)
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def add_course(request):
    for key, value in request.session.items():
            print('{} => {}'.format(key, value))
    course = Courses.objects.all()
    context = {
        'courses':course
    }
    return render(request, "hod_template/add_course_template.html",context)


@login_required(login_url=LOGIN_REDIRECT_URL)
#####@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def add_course_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('add_course')
    else:
        course = request.POST.get('course')
        course_number = request.POST.get('coursenumber')
        try:
            course_model = Courses(course_name=course,course_number=course_number)
            course_model.save()
            messages.success(request, "Course Added Successfully!")
            return redirect('add_course')
            # return HttpResponse('add_course')
        except:
            messages.error(request, "Failed to Add Course!")
            # return redirect('')


@login_required(login_url=LOGIN_REDIRECT_URL)
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def manage_course(request):
    courses = Courses.objects.all()
    context = {
        "courses": courses
    }
    return render(request, 'hod_template/manage_course_template.html', context)


@login_required(login_url=LOGIN_REDIRECT_URL)
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def edit_course(request, course_id):
    course = Courses.objects.get(course_id=course_id)
    context = {
        "course": course,
        "course_id": course_id
    }
    return render(request, 'hod_template/edit_course_template.html', context)

@login_required(login_url=LOGIN_REDIRECT_URL)
#####@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def edit_course_save(request):
    if request.method != "POST":
        HttpResponse("Invalid Method")
    else:
        course_id = request.POST.get('course_id')
        course_name = request.POST.get('newcourse')
        course_number = request.POST.get('newcoursenum')

        try:
            course = Courses.objects.get(id=course_id)
            course.course_name = course_name
            course.course_number = course_number
            course.save()

            messages.success(request, "Course Updated Successfully.")
            return redirect('/edit_course/'+course_id)

        except:
            messages.error(request, "Failed to Update Course.")
            return redirect('/edit_course/'+course_id)


@login_required(login_url=LOGIN_REDIRECT_URL)
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def delete_course(request, course_id):
    course = Courses.objects.get(id=course_id)
    try:
        course.delete()
        messages.success(request, "Course Deleted Successfully.")
        return redirect('manage_course')
    except:
        messages.error(request, "Failed to Delete Course.")
        return redirect('manage_course')


@login_required(login_url=LOGIN_REDIRECT_URL)
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def add_officers(request):
    course = Courses.objects.all()
    storetype = StoreTypes.objects.all()
    customer = Customers.objects.all()
    print('11111')
    print(customer)
    states = States.objects.all()
    context = {
        'courses':course,
        'storetypes':storetype,
        'customers':customer,
        'states':states
    }
    return render(request, "hod_template/add_officers.html",context)

def add_officers_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('add_officers')
    else:
        pno = request.POST.get('pno').upper()
        name = request.POST.get('name')
        rank = request.POST.get('rank')
        branch = request.POST.get('branch')
        cadre = request.POST.get('cadre')
        specialisation = request.POST.get('specialisation')
        commission = request.POST.get('commission')
        appointment = request.POST.get('appointment')
        qualification = request.POST.get('qualification')
        acq1 = request.POST.get('acq1')
        acq2 = request.POST.get('acq2')
        acq3 = request.POST.get('acq3')
        course_1 = request.POST.get('course1')
        course_1_status = request.POST.get('course1_status')
        course_2 = request.POST.get('course2')
        course_2_status = request.POST.get('course2_status')
        course_3 = request.POST.get('course3')
        course_3_status = request.POST.get('course3_status')
        course_4 = request.POST.get('course4')
        course_4_status = request.POST.get('course4_status')
        course_5 = request.POST.get('course5')
        course_5_status = request.POST.get('course5_status')
        doj = request.POST.get('doj')
        station = request.POST.get('station')
        doj_station = request.POST.get('doj_station')
        seniority = request.POST.get('sublt_seniority')
        unit = request.POST.get('unit')
        medical_category = request.POST.get('medical_category')
        dob = request.POST.get('dob')
        doc = request.POST.get('doc')
        dor = request.POST.get('dor')
        dol = request.POST.get('dol')
        dos = request.POST.get('dos')
        spouse_name = request.POST.get('spouse_name')
        afloat_ashore = request.POST.get('afloat_ashore')
        gender = request.POST.get('gender')
        marital_status = request.POST.get('marital_status')
        cmd_sce_result = request.POST.get('cmd_sce_result')
        chance_sce = request.POST.get('chance_sce')
        special_child = request.POST.get('special_child')
        sublt_seniority = request.POST.get('sublt_seniority')
        spouse_nationality = request.POST.get('spouse_nationality')
        special_child = request.POST.get('special_child')
        state = request.POST.get('state')
        pr_applied_yn = request.POST.get('pr_applied_yn')
        resettled_yn = request.POST.get('resettled_yn')
        remarks = request.POST.get('remarks')

        if PersonnelMasters.objects.filter(pno=pno):
            messages.error(request, "Officer exists !")
            return redirect('add_officers')
        else:
            

        # try:
        #     personnelmaster = PersonnelMasters.objects.get(pno=pno)
        #     print('2222222')
        #     print(personnelmaster.pno)
        # except:
        #     pass
        # if not PersonnelMasters.objects.filter(pno=pno):
        #     transfermodel = Transfers (
        #         pno = pno,
        #         name = name, 
        #         rank = rank,
        #         present_unit = unit,
        #         present_appointment = appointment,
        #         pu_outgoing_yn = "N",
        #         status = 0,
        #     )
        #     print('1111111111111')
        #     print(pno)
        #     transfermodel.save()
        #     transfersmaster = Transfers.objects.all().filter(pno=pno)
        #     print(transfersmaster)
        #     transfertrailsmodel = TransferTrails(
        #                         transfers_id = transfersmaster,
        #                         pno = pno,
        #                         name = name, 
        #                         rank = rank,
        #                         present_unit = unit,
        #                         present_appointment = appointment,
        #                         pu_outgoing_yn = "N",
        #                         status = 0,
        #     )
        #     transfertrailsmodel.save()
            personnelmasters_model = PersonnelMasters(
                pno = pno,
                name = name,
                rank = rank,
                branch =branch,
                cadre = cadre,
                specialisation = specialisation,
                commission_type = commission,
                appointment = appointment,
                qualification = qualification ,
                aircraft_qualification_1 = acq1,
                aircraft_qualification_2 = acq2,
                aircraft_qualification_3 = acq3,
                courses_1 =  course_1,
                course_1_status = course_1_status,
                courses_2 = course_2,
                course_2_status = course_2_status,
                courses_3 = course_3,
                course_3_status = course_3_status,
                courses_4 = course_4,
                course_4_status = course_4_status,
                courses_5 = course_5,
                course_5_status = course_5_status,
                doj = doj,
                station = station,
                doj_station = doj_station,
                seniority_in_rank = seniority,
                unit = unit,
                medical_category = medical_category,
                dob = dob,
                date_of_commission = doc,
                date_of_retirement = dor,
                date_of_leaving_service = dol,
                date_of_superannuation = dos,
                marital_status = marital_status,
                spouse_name = spouse_name,
                afloat_ashore = afloat_ashore,
                gender = gender,
                special_child_yn = special_child,
                sublt_seniority = sublt_seniority,
                spouse_nationality = spouse_nationality,
                state = state,
                pr_applied_yn = pr_applied_yn,
                resettled_yn = resettled_yn,
                remarks = remarks,
            )
            personnelmasters_model.save()
            
            messages.success(request, "Officer Added Successfully!")
            return redirect('add_officers')
            # return HttpResponse('add_course')
        # except:
        #     messages.error(request, "Failed to Add Course!")
        #     return redirect('add_officers')


# @login_required(login_url=LOGIN_REDIRECT_URL)
# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
def manage_commission(request):
    personnelmaster = PersonnelMasters.objects.all()
    # for p in personnelmaster:
    print(personnelmaster)
    context = {
        "personnelmaster": personnelmaster
    }
    return render(request, 'hod_template/manage_commission_template.html', context)


# @login_required(login_url=LOGIN_REDIRECT_URL)
# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
def edit_commission(request,personnel_id):
    personnelmaster = PersonnelMasters.objects.get(personnel_id=personnel_id)
    context = {
        "personnelmaster": personnelmaster,
        "personnel_id": personnel_id
    }
    return render(request, 'hod_template/edit_commission_template.html', context)

@login_required(login_url=LOGIN_REDIRECT_URL)
# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
def edit_commission_save(request,personnel_id):
    
    if request.method != "POST":
        HttpResponse("Invalid Method")
    else:
        personnelmaster = PersonnelMasters.objects.get(personnel_id=personnel_id)
        new_commission = request.POST.get('new_commission')
        personnel_id = request.POST.get('personnel_id')
        if personnelmaster.commission_type == "PC":
            messages.error(request, "Commission of a permanent commissioned officer can not be updated")
            return redirect('/edit_commission/'+personnel_id)
        try:
            personnelmaster = PersonnelMasters.objects.get(personnel_id=personnel_id)
            personnelmaster.commission_type = new_commission
            personnelmaster.save()

            messages.success(request, "Commission Updated Successfully.")
            return redirect('/edit_commission/'+personnel_id)

        except:
            messages.error(request, "Failed to Update commission.")
            return redirect('/edit_commission/'+personnel_id )


def upd_cdr_to_capt(request):
    return render(request, "home.html")


def manage_transfer(request):
    transfer = Transfers.objects.all()
    personnelmaster = PersonnelMasters.objects.all()
    context = {
        "transfers" : transfer,
        "personnelmasters":personnelmaster,
    }
    return redirect()
    # return render(request, "hod_template/manage_transfer_template.html", context)

def manage_transfer_action(request,personnel_id):
    transfer = Transfers.objects.all()
    customer = Customers.objects.all()
    personnelmaster = PersonnelMasters.objects.get(personnel_id=personnel_id)
    context = {
        "transfers" : transfer,
        "personnelmasters":personnelmaster,
        "customers" : customer
    }
    return render(request, "hod_template/manage_transfer_action_template.html", context)

def manage_transfer_save(request):
    if request.method != "POST":
        HttpResponse("Invalid Method")
    else:
        personnel_id = request.POST.get('personnel_id')
        proposed_unit = request.POST.get('personnel_id')
        proposed_appointment = request.POST.get('proposed_appointment')
        dtbr = request.POST.get('dtbr')
        pno = request.POST.get('pno')
        transfer_var = Transfers.objects.get(pno=pno)
        personnelmaster = PersonnelMasters.obejcts.get(personnel_id=personnel_id)
        if transfer_var:
            messages.error(request, "Officer already marked for a transfer. Cancel the transfer to proceed")
            return redirect('/manage_transfer_action/'+personnel_id)
        else:
            try:
                transfer = Transfers.objects.get(pno=pno)
                
                transfer.pno = personnelmaster.pno
                transfer.name = personnelmaster.name
                transfer.rank = personnelmaster.rank
                transfer.present_unit = personnelmaster.present_unit
                transfer.present_appointment = personnelmaster.present_appointment
                transfer.pu_outgoing_yn = "N"
                transfer.proposed_unit = proposed_unit
                transfer.porposed_appointment = porposed_appointment
                transfer.dtbr = dtbr
                transfer.status = 1
                transfer.date_initiated = datetime.now()
                transfer.save()

                messages.success(request, "Course Updated Successfully.")
                return redirect('manage_transfer')

            except:
                messages.error(request, "Failed to Update Course.")
                return redirect('manage_transfer')

def mark_transfer_order_out(request):
    return render(request, "home.html")


def mark_officer_reported(request):
    return render(request, "home.html")


def manage_transfer(request):
    return render(request, "home.html")

    
def define_unit_acq_billets(request):
    return render(request, "home.html")


def manage_unit_acq_billets(request):
    return render(request, "home.html")


def mark_officers_for_courses(request):
    return render(request, "home.html")


def amend_marked_courses(request):
    return render(request, "home.html")


def authorise_assigned_course(request):
    return render(request, "home.html")


def mark_compassionate_grounds(request):
    return render(request, "home.html")


def add_details_of_retired_officers(request):
    return render(request, "home.html")


def mark_officers_under_check(request):
    return render(request, "home.html")



def master_officers_view(request):
    personnelmasters = PersonnelMasters.objects.all()
    myFilter = MasterOfficersFilter(request.POST,queryset = personnelmasters)
    personnelmasters = myFilter.qs
    context = {
        "personnelmasters" : personnelmasters,
        "myFilter" : myFilter
        
    }
    return render(request,'hod_template/master_officers_template.html', context)

# @login_required(login_url=LOGIN_REDIRECT_URL)
# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
# def add_student(request):
#     # form = AddStudentForm()
#     storetypes = StoreTypes.objects.all()
#     course = Courses.objects.all()
#     students = HrmUsers.objects.all()
#     context = {
#         # "form": form,
#         "courses":course,
#         "students":students,
#         "storetypes":storetypes
#     }
#     return render(request, 'hod_template/add_student_template.html', context)


# @login_required(login_url=LOGIN_REDIRECT_URL)
# #####@cache_control(no_cache=True, must_revalidate=True, no_store=True)
# def add_student_save(request):
#     if request.method != "POST":
#         messages.error(request, "Invalid Method!")
#         return redirect('add_student')
#     else:
#         pno = request.POST.get('pno')
#         name = request.POST.get('name')
#         rank = request.POST.get('rank')
#         course = request.POST.get('course')
#         course_number = request.POST.get('coursenumber')
#         course_id = request.POST.get('course_id')
#         doj = request.POST.get('doj')
#         industryexp = request.POST.get('industryexp')
#         industryexpyrs = request.POST.get('industryexpyrs')
#         primaryaircraft_id = request.POST.get('primaryaircraft')
#         secondaryaircraft_id = request.POST.get('secondaryaircraft')
#         course_obj = Courses.objects.get(course_id=course_id)
#         primaryaircraft = StoreTypes.objects.get(storetype_id=primaryaircraft_id)
#         secondaryaircraft = StoreTypes.objects.get(storetype_id=secondaryaircraft_id)

#         try:
#             user = HrmUsers.objects.create_user(pno=pno,
#                                             username=pno,
#                                             name=name,
#                                             rank=rank,
#                                             course_id=course_obj,
#                                             date_of_joining=doj,
#                                             industry_exp=industryexp,
#                                             industry_exp_yrs=industryexpyrs,
#                                             primary_aircraft = primaryaircraft.aircraft_name,
#                                             secondary_aircraft = secondaryaircraft.aircraft_name,
#                                             user_type=2) 
#             user.save()
#             messages.success(request, "Student Added Successfully!")
#             return redirect('add_student')
#         except:
#                 messages.error(request, "Failed to Add Student!")
#                 return redirect('add_student')
    
    

#     # if request.method != "POST":
#     #     messages.error(request, "Invalid Method")
#     #     return redirect('add_student')
#     # else:
#     #     form = AddStudentForm(request.POST, request.FILES)

#     #     if form.is_valid():
#     #         first_name = form.cleaned_data['first_name']
#     #         last_name = form.cleaned_data['last_name']
#     #         username = form.cleaned_data['username']
#     #         email = form.cleaned_data['email']
#     #         password = form.cleaned_data['password']
#     #         address = form.cleaned_data['address']
#     #         session_year_id = form.cleaned_data['session_year_id']
#     #         course_id = form.cleaned_data['course_id']
#     #         gender = form.cleaned_data['gender']

#     #         # if len(request.FILES) != 0:
#     #         #     profile_pic = request.FILES['profile_pic']
#     #         #     fs = FileSystemStorage()
#     #         #     filename = fs.save(profile_pic.name, profile_pic)
#     #         #     profile_pic_url = fs.url(filename)
#     #         # else:
#     #         #     profile_pic_url = None

#     #         try:
#     #             user = HrmUsers.objects.create_user(username=username,
#     #                                                   password=password,
#     #                                                   email=email,
#     #                                                   first_name=first_name,
#     #                                                   last_name=last_name,
#     #                                                   user_type=3)
#     #             # user.students.address = address

#     #             course_obj = Courses.objects.get(id=course_id)
#     #             # user.students.course_id = course_obj

#     #             session_year_obj = SessionYearModel.objects.get(
#     #                 id=session_year_id)
#     #             # user.students.session_year_id = session_year_obj

#     #             # user.students.gender = gender
#     #             # user.students.profile_pic = profile_pic_url
#     #             user.save()
#     #             messages.success(request, "Student Added Successfully!")
#     #             return redirect('add_student')
#     #         except:
#     #             messages.error(request, "Failed to Add Student!")
#     #             return redirect('add_student')
#     #     else:
#     #         return redirect('add_student')


# @login_required(login_url=LOGIN_REDIRECT_URL)
# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
# def manage_student(request):
#     students = HrmUsers.objects.filter(user_type=2)
#     context = {
#         "students": students
#     }
#     return render(request, 'hod_template/manage_student_template.html', context)


# @login_required(login_url=LOGIN_REDIRECT_URL)
# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
# def edit_student(request, hrmuserid):

#     students = HrmUsers.objects.get(hrmuserid=hrmuserid)
#     storetypes = StoreTypes.objects.all()
#     context = {
#         "students": students,
#         "hrmuserid": hrmuserid,
#         "storetypes":storetypes
#     }
#     return render(request, "hod_template/edit_student_template.html", context)


# @login_required(login_url=LOGIN_REDIRECT_URL)
# #####@cache_control(no_cache=True, must_revalidate=True, no_store=True)
# def edit_student_save(request):
#     if request.method != "POST":
#         return HttpResponse("Invalid Method!")
#     else:
#         hrmuserid = request.session.get('hrmuserid')
#         if hrmuserid == None:
#             return redirect('/manage_student')

#         newpno = request.POST.get('newpno')
#         newname = request.POST.get('newname')
#         newrank = request.POST.get('newrank')
#         newdoj = request.POST.get('newdoj')
#         newnewindustryexp = request.POST.get('newnewindustryexp')
#         newindustryexpyrs = request.POST.get('newindustryexpyrs')
#         newprimaryaircraft_id = request.POST.get('newprimaryaircraft')
#         newsecondaryaircraft_id = request.POST.get('newsecondaryaircraft')

#         primaryaircraft = StoreTypes.objects.get(storetype_id=newprimaryaircraft_id)
#         secondaryaircraft = StoreTypes.objects.get(storetype_id=newsecondaryaircraft_id)

#         student_original = HrmUsers.objects.filter(hrmuserid=hrmuserid)

#         if newpno == None:
#             print(student_original.pno)
#             # newpno == student_original.pno
#         # elif newname == None:
#         #     newname == student_original.name
#         # elif newrank == None:
#         #     newrank == student_original.rank
#         # elif newdoj == None:
#         #     newdoj == student_original.date_of_joining
#         # elif newnewindustryexp == None:
#         #     newnewindustryexp == student_original.industry_exp
#         # elif newindustryexpyrs == None:
#         #     newindustryexpyrs == student_original.industry_exp_yrs

#         try:
#             student = HrmUsers.objects.get(hrmuserid=hrmuserid)
#             student.pno = newpno
#             student.name = newname
#             student.rank = newrank
#             student.date_of_joining = newdoj
#             student.industry_exp = newnewindustryexp
#             student.industry_exp_yrs = newindustryexpyrs
#             student.primary_aircraft = newprimaryaircraft.aircraft_name
#             student.secondary_aircraft = newsecondaryaircraft.aircraft_name
#             student.save()

#             # Delete student_id SESSION after the data is updated
#             del request.session['student_id']
#             messages.success(request, "Course Updated Successfully.")
#             return redirect('/edit_student/'+hrmuserid)

#         except:
#             messages.error(request, "Failed to Update Course.")
#             return redirect('/edit_student/'+hrmuserid)


# @login_required(login_url=LOGIN_REDIRECT_URL)
# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
# def delete_student(request, hrmuserid):
#     student = HrmUsers.objects.get(hrmuserid=hrmuserid)
#     try:
#         student.delete()
#         messages.success(request, "Student Deleted Successfully.")
#         return redirect('manage_student')
#     except:
#         messages.error(request, "Failed to Delete Student.")
#         return redirect('manage_student')


# @login_required(login_url=LOGIN_REDIRECT_URL)
# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
# def add_ato_results(request):
#     # form = AddStudentForm()
#     course = Courses.objects.all()
#     students = HrmUsers.objects.all()
#     atoresults = AtoResults.objects.all()
#     context = {
#         # "form": form,
#         "courses":course,
#         "students":students,
#         "atoresults":atoresults
#     }
#     return render(request, 'hod_template/add_ato_results_template.html', context)


# @login_required(login_url=LOGIN_REDIRECT_URL)
# #####@cache_control(no_cache=True, must_revalidate=True, no_store=True)
# def add_ato_results_save(request):
#     if request.method != "POST":
#         messages.error(request, "Invalid Method!")
#         return redirect('add_ato_results')
#     else:
#         pno = request.POST.get('pno')
#         name = request.POST.get('name')
#         rank = request.POST.get('rank')
#         p1percent = request.POST.get('p1percent')
#         p2percent = request.POST.get('p2percent')
#         subpercent = request.POST.get('subpercent')
#         ojtpercent = request.POST.get('ojtpercent')
#         hrmuserid = request.POST.get('hrmuserid')
#         hrmusers_obj = HrmUsers.objects.get(hrmuserid=hrmuserid)
#         try:
#             user = HrmUsers.objects.create_user(pno=pno,
#                                             username=pno,
#                                             name=name,
#                                             rank=rank,
#                                             hrmuserid=hrmusers_obj,
#                                             p1_percentage=p1percent,
#                                             p2_percentage=p2percent,
#                                             ojt_percentage=ojtpercent,
#                                             subcourses_percentage=subpercent) 
#             user.save()
#             messages.success(request, "Result Added Successfully!")
#             return redirect('add_ato_results')
#         except:
#                 messages.error(request, "Failed add result")
#                 return redirect('add_ato_results')


# @login_required(login_url=LOGIN_REDIRECT_URL)
# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
# def manage_ato_results(request):
#     atoresults = AtoResults.objects.all()
#     context = {
#         "atoresults": atoresults
#     }
#     return render(request, 'hod_template/manage_ato_results_template.html', context)  


# @login_required(login_url=LOGIN_REDIRECT_URL)
# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
# def edit_ato_results(request, ato_result_id):
#     atoresults = AtoResults.objects.get(ato_result_id=ato_result_id)
#     context = {
#         "atoresults": atoresults,
#         "ato_result_id": ato_result_id
#     }
#     return render(request, 'hod_template/edit_ato_results_template.html', context)


# @login_required(login_url=LOGIN_REDIRECT_URL)
# #####@cache_control(no_cache=True, must_revalidate=True, no_store=True)
# def edit_ato_results_save(request):
#     if request.method != "POST":
#         HttpResponse("Invalid Method")
#     else:
#         ato_result_id = request.POST.get('ato_result_id')
#         newp1percent = request.POST.get('newp1percent')
#         newp2percent = request.POST.get('newp2percent')
#         newsubpercent = request.POST.get('newsubpercent')
#         newojtpercent = request.POST.get('newojtpercent')

#         try:
#             atoresults = AtoResults.objects.get(ato_result_id=ato_result_id)
#             atoresults.p1_percentage = newp1percent
#             atoresults.p2_percentage = newp2percent
#             atoresults.subcourses_percentage = newsubpercent
#             atoresults.ojt_percentage = newojtpercent
#             atoresults.save()

#             messages.success(request, "Course Updated Successfully.")
#             return redirect('/edit_ato_results/'+ato_result_id)

#         except:
#             messages.error(request, "Failed to Update Course.")
#             return redirect('/edit_ato_results/'+ato_result_id)


# @login_required(login_url=LOGIN_REDIRECT_URL)
# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
# def delete_ato_results(request, ato_result_id):
#     atoresults = AtoResults.objects.get(ato_result_id=ato_result_id)
#     try:
#         atoresults.delete()
#         messages.success(request, "Result Deleted Successfully.")
#         return redirect('manage_ato_results')
#     except:
#         messages.error(request, "Failed to Delete results.")
#         return redirect('manage_ato_results')


   

# @csrf_exempt
# def check_email_exist(request):
#     email = request.POST.get("email")
#     user_obj = HrmUsers.objects.filter(email=email).exists()
#     if user_obj:
#         return HttpResponse(True)
#     else:
#         return HttpResponse(False)


# @csrf_exempt
# def check_username_exist(request):
#     username = request.POST.get("username")
#     user_obj = CustomUser.objects.filter(username=username).exists()
#     if user_obj:
#         return HttpResponse(True)
#     else:
#         return HttpResponse(False)


# def student_feedback_message(request):
#     feedbacks = FeedBackStudent.objects.all()
#     context = {
#         "feedbacks": feedbacks
#     }
#     return render(request, 'hod_template/student_feedback_template.html', context)


# @csrf_exempt
# def student_feedback_message_reply(request):
#     feedback_id = request.POST.get('id')
#     feedback_reply = request.POST.get('reply')

#     try:
#         feedback = FeedBackStudent.objects.get(id=feedback_id)
#         feedback.feedback_reply = feedback_reply
#         feedback.save()
#         return HttpResponse("True")

#     except:
#         return HttpResponse("False")


# def staff_feedback_message(request):
#     feedbacks = FeedBackStaffs.objects.all()
#     context = {
#         "feedbacks": feedbacks
#     }
#     return render(request, 'hod_template/staff_feedback_template.html', context)


# @csrf_exempt
# def staff_feedback_message_reply(request):
#     feedback_id = request.POST.get('id')
#     feedback_reply = request.POST.get('reply')

#     try:
#         feedback = FeedBackStaffs.objects.get(id=feedback_id)
#         feedback.feedback_reply = feedback_reply
#         feedback.save()
#         return HttpResponse("True")

#     except:
#         return HttpResponse("False")


# def student_leave_view(request):
#     leaves = LeaveReportStudent.objects.all()
#     context = {
#         "leaves": leaves
#     }
#     return render(request, 'hod_template/student_leave_view.html', context)


# def student_leave_approve(request, leave_id):
#     leave = LeaveReportStudent.objects.get(id=leave_id)
#     leave.leave_status = 1
#     leave.save()
#     return redirect('student_leave_view')


# def student_leave_reject(request, leave_id):
#     leave = LeaveReportStudent.objects.get(id=leave_id)
#     leave.leave_status = 2
#     leave.save()
#     return redirect('student_leave_view')


# def staff_leave_view(request):
#     leaves = LeaveReportStaff.objects.all()
#     context = {
#         "leaves": leaves
#     }
#     return render(request, 'hod_template/staff_leave_view.html', context)


# def staff_leave_approve(request, leave_id):
#     leave = LeaveReportStaff.objects.get(id=leave_id)
#     leave.leave_status = 1
#     leave.save()
#     return redirect('staff_leave_view')


# def staff_leave_reject(request, leave_id):
#     leave = LeaveReportStaff.objects.get(id=leave_id)
#     leave.leave_status = 2
#     leave.save()
#     return redirect('staff_leave_view')


# def admin_view_attendance(request):
#     subjects = Subjects.objects.all()
#     session_years = SessionYearModel.objects.all()
#     context = {
#         "subjects": subjects,
#         "session_years": session_years
#     }
#     return render(request, "hod_template/admin_view_attendance.html", context)


# @csrf_exempt
# def admin_get_attendance_dates(request):

#     subject_id = request.POST.get("subject")
#     session_year = request.POST.get("session_year_id")

#     # Students enroll to Course, Course has Subjects
#     # Getting all data from subject model based on subject_id
#     subject_model = Subjects.objects.get(id=subject_id)

#     session_model = SessionYearModel.objects.get(id=session_year)
#     attendance = Attendance.objects.filter(subject_id=subject_model,
#                                            session_year_id=session_model)

#     # Only Passing Student Id and Student Name Only
#     list_data = []

#     for attendance_single in attendance:
#         data_small = {"id": attendance_single.id,
#                       "attendance_date": str(attendance_single.attendance_date),
#                       "session_year_id": attendance_single.session_year_id.id}
#         list_data.append(data_small)

#     return JsonResponse(json.dumps(list_data),
#                         content_type="application/json",
#                         safe=False)


# @csrf_exempt
# def admin_get_attendance_student(request):

#     # Getting Values from Ajax POST 'Fetch Student'
#     attendance_date = request.POST.get('attendance_date')
#     attendance = Attendance.objects.get(id=attendance_date)

#     attendance_data = AttendanceReport.objects.filter(attendance_id=attendance)
#     # Only Passing Student Id and Student Name Only
#     list_data = []

#     for student in attendance_data:
#         data_small = {"id": student.student_id.admin.id,
#                       "name": student.student_id.admin.first_name+" "+student.student_id.admin.last_name,
#                       "status": student.status}
#         list_data.append(data_small)

#     return JsonResponse(json.dumps(list_data), content_type="application/json", safe=False)


# def admin_profile(request):
#     user = CustomUser.objects.get(id=request.user.id)

#     context = {
#         "user": user
#     }
#     return render(request, 'hod_template/admin_profile.html', context)


# def admin_profile_update(request):
#     if request.method != "POST":
#         messages.error(request, "Invalid Method!")
#         return redirect('admin_profile')
#     else:
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         password = request.POST.get('password')

#         try:
#             customuser = CustomUser.objects.get(id=request.user.id)
#             customuser.first_name = first_name
#             customuser.last_name = last_name
#             if password != None and password != "":
#                 customuser.set_password(password)
#             customuser.save()
#             messages.success(request, "Profile Updated Successfully")
#             return redirect('admin_profile')
#         except:
#             messages.error(request, "Failed to Update Profile")
#             return redirect('admin_profile')


# def staff_profile(request):
#     pass


# def student_profile(requtest):
#     pass
