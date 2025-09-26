from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='Home'),
    # path('sub/',views.sub,name='sub '),
    path('donatepage/',views.donate,name='donatep'),
    path('about/',views.about,name='about'),
    path('services/',views.services,name='services'),
    path('contact/',views.contact,name='contact'),
    path('join_w_us/',views.join_w_us,name='join_w_us'),
    path('loginS/', views.login_view, name='logins'),
    path('donatebuttons/',views.donatebuttons,name='donatebuttons'),
    path('complaints/',views.complaint,name='complaint'),
    path('Adminview/',views.Adminview,name='Adminview'),
    path('data/',views.Data,name='Data'),
    
    path('donation_form/', views.donation_form, name='donation_form'),
    path('success/', views.donation_success, name='donation_success'),
    path('donatefood/',views.donatefood,name='donatefood'),

    path('regis/',views.regis,name='regis'),

    path('money-donation/', views.money_donation_form, name='money_donation_form'),
    path('money-donation/success/', views.money_donation_success, name='money_donation_success'),

    path('donatemoney/',views.donatemoney,name='donatemoney'),


    path('register/', views.register, name='register'),
    path('login/', views.Alogin, name='alogin'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('ASHRAM_approval/', views.ASHRAM_approval, name='admin_approval'),
    path('approve-ashram/<int:ashram_id>/', views.approve_ashram, name='approve_ashram'),
    path('reject-ashram/<int:ashram_id>/', views.reject_ashram, name='reject_ashram'),

    path('approved-ashrams/', views.approved_ashrams, name='approved_ashrams'),

   path('ashram-food-order/', views.ashram_food_order, name='ashram_food_order'),

   path('alllogin/',views.alllogin,name='alllogin'),
   path('approvalData/',views.Allaprove,name='approvalData'),



 

#Function

path('Fregister/',views.Fregister,name='Fregister'),
# path('Fsuccess/',views.Fsuccess,name='Fsuccess'),
path('Flogin/',views.Flogin,name='Flogin'),
    

path('Functionhall_approval/', views.Functionhall_approval, name='Functionhall_approval'),
path('approve_functionhall/<int:fun_id>/', views.approve_functionhall, name='approve_functionhall'),
path('reject-functionhall/<int:fun_id>/', views.reject_functionhall, name='reject_functionhall'),
path('approved_functionhalls/',views.approved_functionhalls,name='approved_functionhalls'),

#volunteer
path('Vregister/',views.Vregister,name='Vregister'),
path('Volunteer_approval/', views.Volunteer_approval, name='Volunteer_approval'),
path('approve_volunteer/<int:vol_id>/', views.approve_volunteer, name='approve_volunteer'),

path('reject_volunteer/<int:vol_id>/', views.reject_volunteer, name='reject_volunteer'),
path('vsuccess/',views.vsuccess,name='vsuccess'),

path('validate_otp/',views.validate_otp,name='validate_otp'),
    path('complaint', views.complaint_view, name='fcomplaint'),
    path('successs/', views.success_view, name='complaintsuccess'),

 path('complaint_list', views.complaint_list_view, name='complaint_list'),
    path('<int:complaint_id>/<str:action>/', views.handle_complaint, name='handle_complaint'),

   path('status/', views.status_buttons_view, name='status_buttons'),
   path('accepted/', views.accepted_complaints_view, name='accepted_complaints'),
    path('solve/<int:complaint_id>/', views.solve_complaint, name='solve_complaint'),

   path('solved/', views.solved_complaints_view, name='solved_complaints'),
  

]