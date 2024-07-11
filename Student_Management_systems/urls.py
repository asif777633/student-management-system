
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .import views,Hod_views,Staff_Views,Student_Views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.BASE,name='base'),

    #Login path
    path('',views.LOGIN,name='login'),
    path('doLogin',views.doLogin,name='doLogin'),
    path('doLogout',views.doLogout,name='logout'),
    path('profile/update',views.PROFILE_UPDATE,name= 'profile_update'),

    # profile Update
    path('profile',views.PROFILE, name='profile'),

# HOD Panel url
    path('Hod/Home',Hod_views.HOME,name='hod_home'),
    path('Hod/Student/Add',Hod_views.ADD_STUDENT,name='add_student'),
    path('Hod/Student/View',Hod_views.VIEW_STUDENT,name= 'view_student'),
    path('Hod/Student/Edit/<str:id>',Hod_views.EDIT_STUDENT,name='edit_student'),
    path('Hod/Student/update',Hod_views.UPDATE_STUDENT,name = 'update_student'),
    path('Hod/Student/Delete/<str:admin>', Hod_views.DELETE_STUDENT,name='delete_student'),
    path('Hod/Staff/Add', Hod_views.ADD_STAFF,name='add_staff'),
    path('Hod/Staff/view', Hod_views.VIEW_STAFF,name='view_staff'),
    path('Hod/Staff/Edit/<str:id>', Hod_views.EDIT_STAFF,name='edit_staff'),
    path('Hod/Staff/Update', Hod_views.UPDATE_STAFF,name='uptadte_staff'),
    path('Hod/Staff/Delete/<str:admin>', Hod_views.DELETE_STAFF,name='delete_staff'),

    path('Hod/Course/Add',Hod_views.Add_COURSE,name = 'add_coures'),
    path('Hod/Course/View', Hod_views.VIEW_COURSE, name='view_course'),
    path('Hod/Course/Edit/<str:id>', Hod_views.EDIT_COURSE, name='eidt_course'),
    path('Hod/Course/update', Hod_views.UPDATE_COURSE, name='update_course'),
    path('Hod/Course/Delete/<str:id>', Hod_views.DELETE_COURSE, name='delete_course'),

    path('Hod/Subject/Add', Hod_views.ADD_SUBJECT, name='add_subject'),
    path('Hod/Subject/view',Hod_views.VIEW_SUBJECT,name = 'view_subject'),
    path('Hod/Subject/edit/<str:id>',Hod_views.EDIT_SUBJECT,name= 'edit_subject'),
    path('Hod/Subject/Update',Hod_views.UPDATE_SUBJECT, name = 'update_subject'),
    path('Hod/Subject/Delete/<str:id>',Hod_views.DELETE_SUBJECT, name = 'delete_subject'),

    path('Hod/Session/Add',Hod_views.ADD_SESSION,name= 'add_session'),
    path('Hod/Session/View,',Hod_views.VIEW_SESSION,name = 'view_session'),
    path('Hod/Session/Edit/<str:id>',Hod_views.EDIT_SESSION, name = 'edit_session'),
    path('Hod/Session/Update',Hod_views.UPDATE_SESSION,name='update_session'),
    path('Hod/Session/Delete/<str:id>' ,Hod_views.DELETE_SESSION,name = 'delete_session'),

    path('Hod/Staff/Send_Notification',Hod_views.STAFF_SEND_NOTIFICATION,name ='staff_send_notification'),
    path('Hod/Staff/save_notification',Hod_views.SAVE_NOTIFICATION,name='save_staff_notification'),



    #this is a Staff url

    path('Staff/Home',Staff_Views.HOME,name = 'staff_home'),
    path('Staff/Notification',Staff_Views.NOTIFICATIONS,name = 'notification'),
    path('Staff/mark_as_done/<str:status',Staff_Views.STAFF_NOTIFICATION_MARK_AS_DONE,name='staff_notification_mark_as_done'),












]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
