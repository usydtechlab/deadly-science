from django.contrib import admin
from django.urls import path,re_path
from django.urls import include
from login import views
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('captcha/', include('captcha.urls')),
    path('confirm/', views.user_confirm),
    path('about/', views.index_about),
    path('index_sci/', views.index_sci),
    path('change_password/', views.change_password),

    path('index/index.html', views.index_home),
    path('index/login/', views.login),
    path('index/register/', views.register),
    path('index/logout/', views.logout),
    path('index_sci/logout', views.logout),
    # path('index_sci/My_account.html', views.index_sci_myaccount),
    # path('index_sci/My_account_change_password.html', views.index_sci_changepassword),
    #
    # path('index_sci/ManageAPP_SCI.html', views.index_sci_manageapp),
    path('index_sci_manageapp/', views.index_sci_manageapp),
    path('My_account_change_password/', views.index_sci_changepassword),
    path('index_account_profile/', views.index_account_profile),
    #
    # path('index_sci/ManageTime_SCI.html', views.index_sci),
    #
    # path('index/account-pw.html', views.index_account_pw),
    # path('index/manageApp-current.html', views.index_manageapp_current),
    # path('index/manageApp-history.html', views.index_manageapp_history),
    # path('index_manageapp_current/', views.index_manageapp_current),
    # path('index_manageapp_history/', views.index_manageapp_history),
    # path('index/about.html', views.index_about),
    # path('index/index-detail.html', views.index_detail),
    # path('index/account-profile.html', views.index_account_profile),
    # path('index/account-pw.html', views.index_account_pw),


    path('index_detail/', views.index_detail),

    # path('index.html', views.index_home),
    # path('manageApp-current.html', views.index_manageapp_current),
    # path('manageApp-history.html', views.index_manageapp_history),
    # path('about.html', views.index_about),
    # path('index-detail.html', views.index_detail),
    # path('account-profile.html', views.index_account_profile),
    # path('index_account_profile/', views.index_account_profile),
    # path('account-pw.html', views.index_account_pw),
    # path('index_account_profile/index.html', views.index),
    # path('index_account_profile/manageApp-current.html', views.index_manageapp_current),
    # path('index_account_profile/about.html', views.index_about),
    # path('index_account_profile/account-profile.html', views.index_account_profile),
    # path('index_account_profile/account-pw.html', views.index_account_pw),
    path('index_sci_myaccount/', views.index_sci_myaccount),
    path('index_manageapp_current/', views.index_manageapp_current),
    path('ManageApp_SCI/', views.index_sci_manageapp),
    path('search/', views.search),

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

    url(r'^indexdetail/(\d+)/$', views.index_detail, name='indexdetail'),
    url(r'^delete_timetable/(\d+)/$', views.delete_timetable, name='delete_timetable'),
    url(r'^makeappointment/(\d+)/$', views.appointment, name='appointment'),
    url(r'^delete_appointment/(\d+)/$', views.delete_appointment, name='delete_appointment'),
    url(r'^confirm/(\d+)/$', views.confirm, name='confirm'),
    url(r'^complete/(\d+)/$', views.complete, name='complete'),
    url(r'^cancel/(\d+)/$', views.cancel, name='cancel'),
    url(r'^reject/(\d+)/$', views.reject, name='reject'),
    url(r'^logout/$', views.logout, name = 'logout'),
    path('', views.index, name='home'),
    path('about', views.index_about, name='about'),
    path('account-profile', views.index_account_profile, name='account-profile'),
    path('account-pw', views.index_account_pw, name='account-pw'),
    path('index_detail', views.index_detail, name='index_detail'),
    path('manageApp-current', views.index_manageapp_current, name='manageApp-current'),
    path('manageApp-history', views.index_manageapp_history, name='manageApp-history'),
    path('ManageApp_SCI', views.index_sci_manageapp, name='ManageApp_SCI'),
    path('ManageTime_SCI', views.index_sci, name='ManageTime_SCI'),
    path('My_account', views.index_sci_myaccount, name='My_account'),
    path('My_account_change_password', views.index_sci_changepassword, name='My_account_change_password'),
    path('search', views.search, name='search'),







]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
