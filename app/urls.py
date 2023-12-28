from django.urls import path
from . import views

urlpatterns = [
       #before login url
       path('register/',views.register,name='register'),
       path('login/',views.handlelogin,name='login'),
       path('login/loginsubmit/',views.loginsubmit,name='loginsubmit'),
       #after login url
       path('home/',views.home,name='home'),
       path('projectview/',views.projectview,name='projectview'),
       path('logout/', views.logout, name='logout'),
       path('myaccount/',views.myaccount,name='myaccount'),
       path('accountdetails/',views.accountdetails,name='accountdetails'),
       path('accountdetails/update_details/', views.update_details, name='update_details'),
       path('yourmembership/',views.yourmembership,name='yourmembership'),
       path('changepassword/',views.changepassword,name='changepassword'),
       path('changepassword/changepasswordbtn/',views.changepasswordbtn,name='changepasswordbtn'),
       path('FAQ/',views.FAQ,name='FAQ'),
       path('settings/',views.settings,name='settings'),
       path('Invoices/',views.Invoices,name='Invoices'),
       path('dashboard/',views.dashboard,name='dashboard'),
       path('projectview/crawling/',views.handlecrawling,name='crawling'),
       path('delete/<int:id>/',views.delete,name='delete'),
       path('projectview/addproject/',views.add,name='add'),
       path('projectview/addproject/addrecord/',views.addrecord,name='addrecord'),
       path('projectview/edit/<int:id>/', views.edit, name='edit'),
       path('projectview/editproject/<int:id>/', views.editrecord, name='editrecord'),
    ]