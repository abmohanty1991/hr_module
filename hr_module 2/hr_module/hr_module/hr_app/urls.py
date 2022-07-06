from django.contrib import admin
from django.urls import path, include
from . import IhqViews, views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('contact', views.contact, name="contact"),
    path('login', views.loginUser, name="login"),
    path('logout_user', views.logout_user, name="logout_user"),
    path('registration', views.registration, name="registration"),
    path('doLogin', views.doLogin, name="doLogin"),
    path('doRegistration', views.doRegistration, name="doRegistration"),
    path('admin_home/', IhqViews.admin_home, name="admin_home"),

    path('add_course/', IhqViews.add_course, name="add_course"),
    path('add_course_save/', IhqViews.add_course_save, name="add_course_save"),
    path('manage_course/', IhqViews.manage_course, name="manage_course"),
    path('edit_course/<course_id>/',IhqViews.edit_course, name="edit_course"),
    path('edit_course_save/', IhqViews.edit_course_save,name="edit_course_save"),
    path('delete_course/<course_id>/',IhqViews.delete_course, name="delete_course"),

    path('add_officers',IhqViews.add_officers, name = "add_officers"),
    path('add_officers_save',IhqViews.add_officers_save, name = "add_officers_save"),
    path('manage_commission',IhqViews.manage_commission, name="manage_commission"),
    path('edit_commission/<personnel_id>',IhqViews.edit_commission, name="edit_commission"),
    path('edit_commission_save',IhqViews.edit_commission_save, name="edit_commission_save"),
    path('upd_cdr_to_capt',IhqViews.upd_cdr_to_capt, name="upd_cdr_to_capt"),
    path('manage_transfer/',IhqViews.manage_transfer, name="manage_transfer"),
    path('manage_transfer_save',IhqViews.manage_transfer_save, name="manage_transfer_save"),
    path('manage_transfer_action/<personnel_id>/',IhqViews.manage_transfer_action, name="manage_transfer_action"),
    path('mark_transfer_order_out',IhqViews.mark_transfer_order_out, name="mark_transfer_order_out"),
    path('mark_officer_reported',IhqViews.mark_officer_reported, name="mark_officer_reported"),
    path('define_unit_acq_billets',IhqViews.define_unit_acq_billets, name="define_unit_acq_billets"),
    path('manage_unit_acq_billets',IhqViews.manage_unit_acq_billets, name="manage_unit_acq_billets"),
    path('mark_officers_for_courses',IhqViews.mark_officers_for_courses, name="mark_officers_for_courses"),
    path('amend_marked_courses',IhqViews.amend_marked_courses, name="amend_marked_courses"),
    path('authorise_assigned_course',IhqViews.authorise_assigned_course, name="authorise_assigned_course"),
    path('mark_compassionate_grounds',IhqViews.mark_compassionate_grounds, name="mark_compassionate_grounds"),
    path('add_details_of_retired_officers',IhqViews.add_details_of_retired_officers, name="add_details_of_retired_officers"),
    path('mark_officers_under_check',IhqViews.mark_officers_under_check, name="mark_officers_under_check"),
    path('master_officers_view',IhqViews.master_officers_view, name="master_officers_view"),
]