from http.client import CannotSendRequest
from secrets import choice
from tokenize import group
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal
from django.core.exceptions import ValidationError
from django.contrib.auth.models import UserManager
# from django.contrib.auth import get_user_model



# from ctypes import DllGetClassObject
# from os import P_NOWAIT, readlink
from unicodedata import name
import unittest
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import GenericIPAddressField


# class SessionYearModel(models.Model):
#     id = models.AutoField(primary_key=True)
#     session_start_year = models.DateField()
#     session_end_year = models.DateField()
#     objects = models.Manager()


# Overriding the Default Django Auth
# User and adding One More Field (user_type)

class States(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=40)

class StoreTypes(models.Model):
    storetype_id = models.AutoField(primary_key=True)
    storetype_abb = models.CharField(max_length=25) # Store type abbreviation
    storetype_name = models.CharField(max_length=25)

class Courses(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=25)
    course_duration_in_weeks = models.IntegerField(default=0)
    # course_number = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True, null = True)
    updated_at = models.DateField(auto_now=True, null = True)
    active_tf = models.BooleanField(default=True)
    objects = models.Manager()

    # def __str__(self):
    #     return self.course_name

class Criteria(models.Model):
    criteria_id = models.AutoField(primary_key=True)
    criteria_name = models.CharField(max_length = 25, null = True)
    criteria_in_rank = models.CharField(max_length = 25, null = True)

class PersonnelMasters(models.Model):
    MALE = "MALE"
    FEMALE = "FEMALE"
    gender_type_data = ((MALE,'MALE'),
                        (FEMALE,'FEMALE'))
    personnel_id = models.AutoField(primary_key=True)
    pno = models.CharField(max_length=25)
    name = models.CharField(max_length=60)
    rank = models.CharField(max_length=25)
    branch = models.CharField(max_length=25)
    cadre = models.CharField(max_length=25)
    specialisation = models.CharField(max_length=25)
    commission_type = models.CharField(max_length=25)
    appointment = models.CharField(max_length=25)
    qualification = models.CharField(max_length=25)
    aircraft_qualification_1 = models.CharField(max_length=25)
    aircraft_qualification_2 = models.CharField(max_length=25, null = True)
    aircraft_qualification_3 = models.CharField(max_length=25, null = True)
    courses_1 = models.IntegerField(default=0, null = True)
    course_1_status = models.CharField(max_length=25, null = True) # Whether completed or undergoing
    courses_2 = models.IntegerField(default=0, null = True)
    course_2_status = models.CharField(max_length=25, null = True) # Whether completed or undergoing
    courses_3 = models.IntegerField(default=0, null = True)
    course_3_status = models.CharField(max_length=25, null = True) # Whether completed or undergoing
    courses_4 = models.IntegerField(default=0, null = True)
    course_4_status = models.CharField(max_length=25, null = True) # Whether completed or undergoing
    courses_5 = models.IntegerField(default=0, null = True)
    course_5_status = models.CharField(max_length=25, null = True) # Whether completed or undergoing
    doj = models.DateField(auto_now=True, null = True)
    station = models.CharField(max_length=25, null = True)
    doj_station = models.DateField(auto_now=True, null = True)
    seniority_in_rank = models.IntegerField(default=0, null = True)
    unit = models.CharField(max_length=25, null = True)
    look_year = models.DateField(auto_now=False, null = True)
    medical_category = models.CharField(max_length=25, null = True)
    dob = models.DateField(auto_now=True, null = True)
    date_of_commission = models.DateField(auto_now=True, null = True)
    date_of_retirement = models.DateField(auto_now=True, null = True)
    date_of_leaving_service = models.DateField(auto_now=True, null = True)
    date_of_superannuation = models.DateField(auto_now=True, null = True)
    marital_status = models.CharField(max_length=25, null = True)
    spouse_name = models.CharField(max_length=60, null = True)
    afloat_ashore = models.CharField(max_length=25, null = True)
    ex_units = models.CharField(max_length=25, null = True)# we need list of units here, consider json
    ex_unit_grp = models.CharField(max_length=25, null = True)
    future_unit = models.CharField(max_length=25, null = True)
    future_appt = models.CharField(max_length=25, null = True)
    dtbr = models.DateField(auto_now=False, null = True)
    duration_in_present_unit = models.IntegerField(default=0, null = True)
    gender = models.CharField(max_length=25,choices=gender_type_data, null = True)
    select_list_year = models.DateField(auto_now=False, null = True)
    chance_selection= models.CharField(max_length=25, null = True)
    command_sce_result = models.CharField(max_length=25, null = True)
    special_child_yn = models.CharField(max_length=25, null = True)
    sea_command_yn = models.CharField(max_length=25, null = True)
    sublt_seniority = models.IntegerField(default=0, null = True)
    special_skills = models.CharField(max_length=25, null = True)
    spouse_nationality = models.CharField(max_length=25, null = True)
    state = models.CharField(max_length=25, null = True)
    station_seniority = models.IntegerField(default=0, null = True)
    pr_applied_yn = models.CharField(max_length=25, null = True)
    resettled_yn = models.CharField(max_length=25, null = True)
    granted_extension = models.CharField(max_length = 20, null = True)
    # Define 10+2 as suppose A and 10+4 as B....accordingly aggregate for views
    remarks = models.CharField(max_length=100, null = True)
    # deputation_abroad_yn
    # dep_cat 
    # dep_details...date and duration
    # Explore json option to include multiple courses 
    # multiple aircraft qualifications as well. 
    # As of now handle 3 aircraft qualifications and 5 courses

    
# class HrmUsers(AbstractUser):
#     JDASE = '1'
#     ACNS = '2'
#     JDASE_STAFF = '3'

#     EMAIL_TO_USER_TYPE_MAP = {
#         'jdase': JDASE,
#         'jdase_staff':JDASE_STAFF,
#         'acns': ACNS,
#     }

#     user_type_data = ((JDASE, "jdase"), (ACNS, "acns"),(JDASE_STAFF,"jdase_staff"))
#     user_type = models.CharField(default=1, choices=user_type_data, max_length=10)
#     id = models.AutoField(primary_key=True)
#     pno = models.CharField(max_length=25)
#     name = models.CharField(max_length=25)
#     rank = models.CharField(max_length=25)
#     # date_of_joining = models.DateField(auto_now=True)
#     # industry_exp = models.CharField(max_length=300)
#     # industry_exp_yrs = models.IntegerField(default=0)
#     # course_id = models.ForeignKey(Courses, on_delete=models.CASCADE, default=1)
#     active_tf = models.BooleanField(default=True)


class PersonnelTagged(models.Model): #personnel under check
    personneltagged_id = models.AutoField(primary_key=True)
    personnel_id = models.ForeignKey(PersonnelMasters, on_delete=models.CASCADE, default=1)
    pno = models.CharField(max_length=25)
    name = models.CharField(max_length=60)
    rank = models.CharField(max_length=25)
    branch = models.CharField(max_length=25)
    cadre = models.CharField(max_length=25)
    specialisation = models.CharField(max_length=25)
    commission_type = models.CharField(max_length=25)
    aircraft_qualification_1 = models.CharField(max_length=25)
    actions_performed_by_person = models.CharField(max_length=200)
    references = models.CharField(max_length=200)
    supporting_documents = models.FileField()   # Decide whether to facilitate uploading of files or not.


class Transfers(models.Model):
    MARKED_FOR_TRANSFER = "1"
    CLEARED_BY_ACNS_AM = "2"
    PENDING_WITH_DOP = "3"
    TRANSFER_ORDER_OUT = "4"
    OFFICER_REPORTED = "5"
    TRANSFER_ORDER_CANCELLED = "6"
    TRANSFER_DELAYED =  "7"

    transfer_type_data = ( 
                        (MARKED_FOR_TRANSFER,'1'),
                        (CLEARED_BY_ACNS_AM,'2'),
                        (PENDING_WITH_DOP,'3'),
                        (TRANSFER_ORDER_OUT,'4'),
                        (OFFICER_REPORTED, '5'),
                        (TRANSFER_ORDER_CANCELLED,'6'),
                        (TRANSFER_DELAYED,'7'),
    )

    
    transfers_id = models.AutoField(primary_key=True)
    pno = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    rank = models.CharField(max_length=25)
    present_unit = models.CharField(max_length=25) # so when the officer reports this present unit gets updated by the newly joined unit name along with present unit in personnelmasters model
    present_appointment = models.CharField(max_length=25)
    pu_outgoing_yn = models.CharField(default="N", max_length=10) # present unit outgoing list y n
    proposed_unit = models.CharField(max_length=25, null=True)
    porposed_appointment = models.CharField(max_length=25, null=True)
    dtbr = models.DateField(auto_now=False, null=True)
    doj_present_unit = models.DateField(auto_now=False,null=True)
    status = models.CharField(default=0,choices=transfer_type_data, max_length=30)
    date_initiated = models.DateField(auto_now=False,null = True)
    date_completed = models.DateField(auto_now=False,null=True)
    reason_cancellation = models.CharField(default=0,max_length=30, null=True)
    reason_delayed = models.CharField(default=0,max_length=30,null=True)
    marked_for_pg = models.CharField(max_length = 10,default = "N", null = True)
    date_marked_for_pg = models.DateField(auto_now=False, null=True)
    # Value will be assigned when an officer is marked for pg
    # Value will only be reverted back to N if the officer reports back from pg
    # Otherwise if the pg allocation is cancelled..... but put a validation between date_marked_for_pg and reporting_back and date_of_remarking

    # file idle at a place for more than 7 days, alert=---- pop up......


class TransferTrails(models.Model):
    transfertrail_id = models.AutoField(primary_key=True)
    # personnel_id = models.ForeignKey(PersonnelMasters,on_delete=models.CASCADE,default=1)
    transfers_id = models.ForeignKey(Transfers,on_delete=models.CASCADE,default=1)
    pno = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    rank = models.CharField(max_length=25)
    appointment = models.CharField(max_length=25)
    from_unit = models.CharField(max_length=25)
    to_unit = models.CharField(max_length=25)
    to_unit_amended_yn = models.CharField(max_length=10)
    designation = models.CharField(max_length=25)
    dtbr = models.DateField(auto_now=False, null = True)
    status = models.CharField(max_length = 30)
    date_of_reporting = models.DateField(auto_now=False, null = True)
    date_initiated = models.DateField(auto_now_add=True, null = True)
    date_completed = models.DateField(auto_now_add=False, null = True)
    reason_cancellation = models.CharField(default=0,max_length=30)
    reason_delayed = models.CharField(default=0,max_length=30)






# A Manager is the interface through which database query operations are provided to Django models.
# At least one Manager exists for every model in a Django application




# # Creating Django Signals
# # Read about Django signals. Important
# @receiver(post_save, sender=CustomUser)
# # Now Creating a Function which will
# # automatically insert data in HOD, Staff or Student
# def create_user_profile(sender, instance, created, **kwargs):
#     # if Created is true (Means Data Inserted)
#     if created:

#         # Check the user_type and insert the data in respective tables
#         if instance.user_type == 1:
#             AdminHOD.objects.create(admin=instance)
#         if instance.user_type == 2:
#             Staffs.objects.create(admin=instance)
#         if instance.user_type == 3:
#             Students.objects.create(admin=instance,
#                                     course_id=Courses.objects.get(id=1),
#                                     session_year_id=SessionYearModel.objects.get(
#                                         id=1),
#                                     address="",
#                                     profile_pic="",
#                                     gender="")


# @receiver(post_save, sender=CustomUser)
# def save_user_profile(sender, instance, **kwargs):
#     if instance.user_type == 1:
#         instance.adminhod.save()
#     if instance.user_type == 2:
#         instance.staffs.save()
#     if instance.user_type == 3:
#         instance.students.save()












# Overriding the Default Django Auth
# User and adding One More Field (user_type)

class Customers(models.Model):

    FRONT_LINE = "front line"
    SECOND_LINE = "second line"
    YARD = "yard"
    MO = "mo"
    QA =  "qa"
    FLIGHT ="flight"
    TRAINING = "training"
    HQNA = "hqna"
    IHQ = "ihq"
    AA = "aa"


    unit_type_data = ( (FRONT_LINE,'front line'),  
                        (SECOND_LINE,'second line'),
                        (YARD,'yard'),
                        (MO,'mo'),
                        (QA, 'qa'),
                        (FLIGHT,'flight'),
                        (TRAINING,'training'),
                        (HQNA,'hqna'),
                        (IHQ,'ihq'),
                        (AA,'aa')
    )
    customer_id = models.AutoField(primary_key = True)
    customer_name =  models.CharField(max_length=25)
    sub_customer_name =  models.CharField(max_length=25)
    unit_type = models.CharField(default=1, choices=unit_type_data, max_length=20)



# class Courses(models.Model):

#     NAVAL = "naval"
#     NON_NAVAL = "non naval"
#     course_type_data = ((NAVAL,'naval'),
#                         (NON_NAVAL,'non naval'),
#                         )
#     course_id = models.AutoField(primary_key=True)
#     course_name = models.CharField(max_length=50)
#     course_number = models.CharField(max_length=50)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     course_type = models.CharField(default=1, choices = course_type_data, max_length=25)
#     active_tf = models.BooleanField(default=True)
#     objects = models.Manager()

    # def __str__(self):
    #     return self.course_name

# class SailorCourses(models.Model):

#     sailor_course_id = models.AutoField(primary_key=True)
#     course_name = models.CharField(max_length=25)
#     course_number = models.CharField(max_length=50)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     active_tf = models.BooleanField(default=True)
#     objects = models.Manager()

# class SailorCoursePapers(models.Model):
#     course_paper_id = models.AutoField(primary_key=True)
#     sailor_course_id = models.ForeignKey(SailorCourses,on_delete=models.CASCADE, default=1)

# class StoreTypes(models.Model):
#     storetype_id = models.AutoField(primary_key=True)
#     store_type = models.CharField(max_length=25)
#     aircraft_name = models.CharField(max_length=25)
#     aircraft_yn = models.CharField(max_length=10)
#     date_commissioned = models.DateTimeField(auto_now_add=True)
#     date_decommissioned = models.DateTimeField(auto_now_add=True)
#     objects = models.Manager()
    
class SecurityQuestions(models.Model):
    secques_id = models.AutoField(primary_key=True)
    security_question = models.CharField(max_length = 300, default=1)
    
class HrmUsers(AbstractUser):
    JDASE = '1'
    ACNS = '2'
    JDASE_STAFF = '3'

    USER_TYPE_MAP = {
        'jdase': JDASE,
        'acns': ACNS,
        'jdase_staff': JDASE_STAFF,
    }
    # AE = "AE"
    # AL = "AL"
    # branch_type_data = ((AE,'AE'),
    #                     (AL,'AL'),
    #                     )
    
    # MALE = "MALE"
    # FEMALE = "FEMALE"

    # gender_type_data = (
    #     (MALE,"MALE"),
    #     (FEMALE, "FEMALE")
    # )

    # S1A1 = "S1A1"
    # S2A2 = "S2A2"
    # S2A1 = "S2A1"
    # S3A2 = "S3A2"
    # S3A3 = "S3A3"
    # S3A1 = "S3A1"
    # S4A4 = "S4A4"
    # S5A5 = "S5A5"
    # S2A2_TEMP = "S2A2 TEMPORARY"
    # S3A2_TEMP = "S3A2 TEMPORARY"
    # medical_cat_type_data = (
    #     (S1A1,"S1A1"),
    #     (S2A1,"S2A1"),
    #     (S2A2,"S2A2"),
    #     (S3A1,"S3A1"),
    #     (S3A2,"S3A2"),
    #     (S3A3,"S3A3"),
    #     (S4A4,"S4A4"),
    #     (S5A5,"S5A5"),
    #     (S2A2_TEMP,"S2A2 TEMPORARY"),
    #     (S3A2_TEMP,"S3A2 TEMPORARY")
    # )

    # SSC = "SSC"
    # PC = "PC"
    # STP = "STP"
     
    # entry_type_data = (
    #     (SSC,"SSC"),
    #     (PC,"PC"),
    #     (STP,"STP")
    # )

    user_type_data = ((JDASE, "jdase"), (ACNS, "acns"), (JDASE_STAFF, "jdase_staff"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)
    hrmuserid = models.AutoField(primary_key=True)
    pno = models.CharField(max_length=25)
    password = models.CharField(max_length=700)
    name = models.CharField(max_length=50)
    rank = models.CharField(max_length=25)
    active_tf = models.BooleanField(default=True)
    objects = models.Manager()
    secques_id = models.ForeignKey(SecurityQuestions, on_delete=models.CASCADE,null=True)
    sec_ques_ans = models.CharField(max_length = 300, default=1)
    # objects = models.Manager()
    objects = UserManager()



# appt history
# courses services and both previous 
# promotion history, sto due on, wet listing due on, pb2 due on .....(mandatory appts)
# forecast sheet for appointments, courses, promotions
# mandatory appts (forecasts table)

# PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]
# PERCENTAGE_SENIORITY_VALIDATOR = [MinValueValidator(0), MaxValueValidator(12)]

# class AtoResults(models.Model):
#     ato_result_id =  models.AutoField(primary_key=True)
#     hrmuserid = models.ForeignKey(HrmUsers,on_delete=models.CASCADE, default=1)
#     p1_percentage = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0), validators=PERCENTAGE_VALIDATOR)
#     p2_percentage = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0), validators=PERCENTAGE_VALIDATOR)
#     ojt_percentage = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0), validators=PERCENTAGE_VALIDATOR)
#     subcourses_percentage = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0), validators=PERCENTAGE_VALIDATOR)
#     seniority_in_months = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0), validators=PERCENTAGE_SENIORITY_VALIDATOR)
#     stream_allotted = models.CharField(max_length=25)
#     aircraft_specialisation = models.CharField(max_length=25)
#     active_tf = models.BooleanField(default=True)
#     objects = models.Manager()

    # Implement separate validations for percentage and seniority in months later. can use below code
    # def validate_ratio(value):
    #     try:
    #         if not (0 <= value <= 100):
    #             raise ValidationError(
    #                 f'{value} must be between 0 and 100', params={'value': value}
    #             )
    #     except TypeError:
    #         raise ValidationError(
    #             f'{value} must be a number', params={'value': value}
    #         )

class Appointments(models.Model):

    ALO = "ALO"
    AEO = "AEO"
    DY_ALO = "DY ALO"
    DY_AEO = "DY_AEO"
    ASST_ALO = "ASST_ALO"
    ASST_AEO = "ASST_AEO"
    STO = "STO"
    SALO = "SALO"
    SAEO = "SAEO"
    CAPT_TECH = "CAPT TECH"
    DIRECTOR = "DIRECTOR"
    DY_DIRECTOR = "DY DIRECTOR"

    appt_type_data = ((ALO,'ALO'),
                    (AEO,'AEO'),
                    (DY_ALO,'DY ALO'),
                    (DY_AEO,'DY_AEO'),
                    (ASST_ALO,'ASST_ALO'),
                    (ASST_AEO,'ASST_AEO'),
                    (STO,'STO'),
                    (SALO,'SALO'),
                    (SAEO,'SAEO'),
                    (CAPT_TECH,'CAPT TECH'),
                    (DIRECTOR,'DIRECTOR'),   
                    (DY_DIRECTOR,'DY DIRECTOR'),
                    )
    # hrmuserid = models.ForeignKey(HrmUsers,on_delete=models.CASCADE, default=1)
    appt_id = models.AutoField(primary_key=True)
    appt_name =  models.CharField(max_length=25)
    customer_id = models.ForeignKey(Customers,on_delete=models.CASCADE, default=1) # essentially sub_customer_name from Customers
    unit_type = models.CharField(max_length=25)
    appt_type = models.CharField(default=1,choices=appt_type_data,max_length=30 )
    active_tf = models.BooleanField(default=True)
    # station
    # sattion date from
    objects = models.Manager()



class UnitMpMasters(models.Model):
    unitmpmasters_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customers,on_delete=models.CASCADE, default=1)
    unit_name = models.CharField(max_length=25)
    unit_group = models.CharField(max_length=25)
    branch = models.CharField(max_length=25)
    rank_wise = models.CharField(max_length=25)
    aircraft = models.CharField(max_length=25)
    manpower_proposed = models.IntegerField(default=0)
    manpower_present = models.IntegerField(default=0)
    total_mp_met_yn = models.CharField(max_length=10)
    rank_and_branch_wise_mp_met_yn = models.CharField(max_length=10)
    acq_wise_mp_met_yn = models.CharField(max_length=10)
    overmanned_by = models.IntegerField(default=0) # Based on total mp
    undermanned_by = models.IntegerField(default=0)# Based on total mp
    updated_by = models.CharField(max_length=10)
    updated_at = models.DateField(auto_now=True, null = True)

class UnitMpTrails(models.Model):
    unitmptrails_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customers,on_delete=models.CASCADE, default=1)
    unit_name = models.CharField(max_length=25)
    unit_group = models.CharField(max_length=25)
    branch = models.CharField(max_length=25)
    rank_wise = models.CharField(max_length=25)
    aircraft = models.CharField(max_length=25)
    manpower_proposed = models.IntegerField(default=0)
    manpower_present = models.IntegerField(default=0)
    overmanned_by = models.IntegerField(default=0)
    undermanned_by = models.IntegerField(default=0)
    updated_by = models.CharField(max_length=20)
    updated_at = models.DateField(auto_now=True, null = True)
    status = models.CharField(max_length=25) #  status will tell what happened
    # which category manpower got increased after allocation or the definition has been changed.
    # 1 - rank_wise allocation updated as per new mp
    # 2 - branch wise allocation updated as per new mp
    # 3 - acq wise allocation updated by jdase
    # 4 - 

    



class UnitAuthorisations(models.Model):
    unit_auth_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE, default=1)
    unit_name = models.CharField(default=1,max_length=30)
    unit_aeo_auth = models.IntegerField(default=0)
    unit_alo_auth = models.IntegerField(default=0)
    unit_aeo_strength = models.IntegerField(default=0)
    unit_alo_strength = models.IntegerField(default=0)
    active_tf = models.BooleanField(default=True)
    objects = models.Manager()

class UnitAuthorisationTrails(models.Model):
    unit_auth_trails_id = models.AutoField(primary_key=True)
    unit_auth_id = models.ForeignKey(UnitAuthorisations,on_delete=models.CASCADE,default=0)
    unit_name = models.CharField(default=1,max_length=30)
    unit_aeo_auth = models.IntegerField(default=0)
    unit_alo_auth = models.IntegerField(default=0)
    unit_aeo_strength = models.IntegerField(default=0)
    unit_alo_strength = models.IntegerField(default=0)
    date_created = models.DateField(auto_now_add=True, null = True)
    active_tf = models.BooleanField(default=True)
    objects = models.Manager()

# # Creating Django Signals
# # Read about Django signals. Important
# @receiver(post_save, sender=CustomUser)
# # Now Creating a Function which will
# # automatically insert data in HOD, Staff or Student
# def create_user_profile(sender, instance, created, **kwargs):
#     # if Created is true (Means Data Inserted)
#     if created:

#         # Check the user_type and insert the data in respective tables
#         if instance.user_type == 1:
#             AdminHOD.objects.create(admin=instance)
#         if instance.user_type == 2:
#             Staffs.objects.create(admin=instance)
#         if instance.user_type == 3:
#             Students.objects.create(admin=instance,
#                                     course_id=Courses.objects.get(id=1),
#                                     session_year_id=SessionYearModel.objects.get(
#                                         id=1),
#                                     address="",
#                                     profile_pic="",
#                                     gender="")


# @receiver(post_save, sender=CustomUser)
# def save_user_profile(sender, instance, **kwargs):
#     if instance.user_type == 1:
#         instance.adminhod.save()
#     if instance.user_type == 2:
#         instance.staffs.save()
#     if instance.user_type == 3:
#         instance.students.save()
