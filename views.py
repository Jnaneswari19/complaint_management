from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseForbidden
from django.template import loader
from django. contrib import messages
from django.contrib.auth import authenticate, login

def regis(request):
  template = loader.get_template('pages/regis_feedback.html')
  return HttpResponse(template.render())

# Create your views here.
#home page
def index(request):
  template = loader.get_template('pages/index.html')
  return HttpResponse(template.render())

#DonateNow page
def donate(request):
  template = loader.get_template('pages/donate.html')
  return HttpResponse(template.render())
#AboutUs
def about(request):
  template = loader.get_template('pages/about_us.html')
  return HttpResponse(template.render())

#OueServices
def services(request):
  template = loader.get_template('pages/our_services.html')
  return HttpResponse(template.render())

#ContactUs
def contact(request):
  template = loader.get_template('pages/contact_us.html')
  return HttpResponse(template.render())

#join_W_Us
def join_w_us(request):
  template = loader.get_template('pages/join_w_us.html')
  return HttpResponse(template.render())

#donatebuttons
def donatebuttons(request):
  template = loader.get_template('pages/donatebutons.html')
  return HttpResponse(template.render())

#complaints_M_M_P
def complaint(request):
  template = loader.get_template('pages/complaints.html')
  return HttpResponse(template.render())

#AdminLogin
from .forms import LoginForm
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request ,user)
                return redirect('Adminview') 
    else:
        form = LoginForm()

    return render(request, 'pages/admin_login.html', {'form': form})




#Admin_view
def Adminview(request):
  template = loader.get_template('pages/adminview.html')
  return HttpResponse(template.render())

#Data_view

def Data(request):
  template = loader.get_template('pages/data.html')
  return HttpResponse(template.render())


#Donation form

from .models import Donation
from django.db.models import F

def donation_form(request):
    if request.method == 'POST':
        form_data = request.POST
        donation = Donation.objects.create(
            name=form_data['name'],
            email=form_data['email'],
            number=form_data['number'],
            Quantity=form_data['Quantity'],
            address=form_data['address']
        )
        return redirect('donation_success')
    return render(request, 'components/donation_form.html')



def donation_success(request):
    
    
    return render(request, 'components/donation_success.html')

def donatefood(request):
    donations = Donation.objects.all()
    context = {'donations': donations}
    return render(request, 'components/Admin_food.html', context)


#money_donation

from .models import MoneyDonation

def money_donation_form(request):
    if request.method == 'POST':
        form_data = request.POST
        donation = MoneyDonation.objects.create(
            name=form_data['name'],
            email=form_data['email'],
            number=form_data['number'],
            amount=form_data['amount'],
            address=form_data['address']
        )
       
        return redirect('money_donation_success')
    return render(request, 'components/money_donation_form.html')

def money_donation_success(request):
    
    
    return render(request, 'components/money_donation_success.html')   

#all login
def alllogin(request):
    
    
    return render(request, 'components/alllogin.html')  

def donatemoney(request):
    money = MoneyDonation.objects.all()
    context = {'donations': money}
    return render(request, 'components/Admin_money.html', context)






#Ashram_regis And Login

from .forms import RegistrationForm, ALoginForm,OTPValidationForm
from .models import Ashram
import random


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            ashram = form.save(commit=False)
            ashram.otp = str(random.randint(100000, 999999))
            ashram.save()
            # Send OTP to ashram.email (not implemented here)
            return HttpResponse('fgfva')
    else:
        form = RegistrationForm()
    return render(request, 'components/register.html', {'form': form})




def Alogin(request):
    if request.method == 'POST':
        form = ALoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            user = Ashram.objects.filter(name=name, password=password).first()
            if user is not None:
                if user.is_approved:
                    return redirect('ashram_food_order')
                else:
                    return HttpResponseForbidden('Your account is not approved yet. Please wait for approval.')
            else:
                return HttpResponse('none')  
              
    else:
        form = ALoginForm()
        messages.warning(request, "Data was not inserted")
    return render(request, 'components/Ashramlogin.html', {'form': form})


def dashboard(request):
    return render(request, 'components/dashboard.html')

def ASHRAM_approval(request):
    ashrams_to_approve = Ashram.objects.filter(is_approved=False)
    return render(request, 'components/admin_approval.html', {'ashrams_to_approve': ashrams_to_approve})

def approve_ashram(request, ashram_id):
    ashram = Ashram.objects.get(id=ashram_id)
    ashram.is_approved = True
    ashram.save()
    return redirect('admin_approval')

def reject_ashram(request, ashram_id):
    ashram = Ashram.objects.get(id=ashram_id)
    ashram.delete()
    return redirect('admin_approval')

def approved_ashrams(request):
    approved_ashrams = Ashram.objects.filter(is_approved=True)
    return render(request, 'components/approved_ashrams.html', {'approved_ashrams': approved_ashrams})


from django.utils import timezone
def ashram_food_order(request):
    # Get all donations within the last 24 hours
    donations = Donation.objects.filter(timestamp__gte=timezone.now() - timezone.timedelta(hours=24))

    total_quantity = sum(donation.Quantity for donation in donations)

    context = {
        'total_quantity': total_quantity
    }
    return render(request, 'components/ashram_food_order.html', context)

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Resets the donated food quantity after 24 hours'

    def handle(self, *args, **kwargs):
        Donation.objects.filter(timestamp__lt=timezone.now() - timezone.timedelta(hours=24)).delete()


# donations/apps.py
from django.apps import AppConfig

class DonationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'donations'

    def ready(self):
        from django.conf import settings
        from django.core.management import call_command

        if not settings.DEBUG:
            # Run the reset_food_quantity command every day at midnight
            call_command('reset_food_quantity')




def Allaprove(request):
  template = loader.get_template('components/Apprvaldata.html')
  return HttpResponse(template.render())





from .forms import FRegistrationForm, FLoginForm ,VRegistrationForm , VLoginForm
from .models import Functionhall
from .utils import *

from django.core.mail import send_mail

def Fregister(request):
    if request.method == 'POST':
        form = FRegistrationForm(request.POST)
        if form.is_valid():
            function = form.save(commit=False)
            email = form.cleaned_data['email']
            otp = generate_otp()
            request.session['otp'] = otp
            send_mail(
                'Your OTP',
                f'Your OTP is : {otp}',
                'from@example.com',
                [email],#to email
                fail_silently=False,
            )
            function.save()
            return redirect('validate_otp')
            
    else:
        form = RegistrationForm()
    return render(request, 'components/Fregister.html', {'form': form})

def validate_otp(request):
    if request.method == 'POST':
       form = OTPValidationForm(request.POST)
       if form.is_valid():
           entered_otp = form.cleaned_data['otp']
           stored_otp = request.session.get('otp')

           if entered_otp == stored_otp:
               return HttpResponse('otp match')
           else:
               return HttpResponse('not match')
    else:
        form = OTPValidationForm()
    return render(request,'components/otp_validation.html',{'form':form})


# def Fsuccess(request):
#      return render(request, 'components/Fsuccess.html')



def Flogin(request):
    if request.method == 'POST':
        form = FLoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            user = Functionhall.objects.filter(name=name, password=password).first()
            if user is not None:
                if user.is_approved:
                    return HttpResponse('ashram_food_order')
                else:
                    return HttpResponseForbidden('Your account is not approved yet. Please wait for approval.')
            else:
                return HttpResponse('none')  
              
    else:
        form = FLoginForm()
        messages.warning(request, "Data was not inserted")
    return render(request, 'components/Flogin.html', {'form': form})



def Functionhall_approval(request):
    FunctionhallAA = Functionhall.objects.filter(is_approved=False)
    return render(request, 'components/Functionhall_approval.html', {'Functionhall': FunctionhallAA})

def approve_functionhall(request, fun_id):
    print("asdfasdfasdf")
    FunctionhallA = Functionhall.objects.get(id=fun_id)
    print(FunctionhallA)
    print("asdfasdfasdf")
    FunctionhallA.is_approved = True
    FunctionhallA.save()
    return redirect('Functionhall_approval')


# def approve_ashram(request, ashram_id):
#     ashram = Ashram.objects.get(id=ashram_id)
#     ashram.is_approved = True
#     ashram.save()
#     return redirect('admin_approval')

def reject_functionhall(request, fun_id):
    FunctionhallR = Functionhall.objects.get(id=fun_id)
    
    FunctionhallR.delete()
    return redirect('Functionhall_approval')

def approved_functionhalls(request):
    approved_Functionhall = Functionhall.objects.filter(is_approved=True)
    

    return render(request, 'components/approved_ashrams.html', {'approved_Functionhall': approved_Functionhall})




#volunteer
from .models import Volunteer

def Vregister(request):
    if request.method == 'POST':
        form = VRegistrationForm(request.POST)
        if form.is_valid():
            volunteer = form.save(commit=False)
            
            volunteer.save()
            
            # Send OTP to ashram.email (not implemented here)
            return redirect('vsuccus')
    else:
        form = RegistrationForm()
    return render(request, 'components/Vregister.html', {'form': form})

def Volunteer_approval(request):
    volunteerAA = Volunteer.objects.filter(is_approved=False)
    return render(request, 'components/Volunteer_approval.html', {'volunteerAA': volunteerAA})

def approve_volunteer(request, vol_id):
    print("asdfasdfasdf")
    volunteer = Volunteer.objects.get(id=vol_id)
    
    volunteer.is_approved = True
    volunteer.save()
    return redirect('Volunteer_approval')

def reject_volunteer(request, vol_id):
    volunteer = Volunteer.objects.get(id=vol_id)
    
    volunteer.delete()
    return redirect('Volunteer_approval')


def vsuccess(request):
  template = loader.get_template('components/vsuccus.html')
  return HttpResponse(template.render())

from .forms import ComplaintForm
from django.conf import settings

def complaint_view(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            # Handle the form data
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            complaint = form.cleaned_data['complaint']

            # Send success email
            # send_mail(
            #     'Complaint Received',
            #     f'Thank you for your complaint, {name}. We will address it as soon as possible.',
            #     settings.DEFAULT_FROM_EMAIL,
            #     [email],
            #     fail_silently=False,
            # )

            # Redirect to the success page
            return redirect('complaintsuccess')
    else:
        form = ComplaintForm()
    
    return render(request, 'components/complaint_form.html', {'form': form})

def success_view(request):
    return render(request, 'components/complaintsuccess.html')

from .models import Complaint

def complaint_list_view(request):
    complaints = Complaint.objects.filter(status='Pending')
    return render(request, 'components/complaint_list.html', {'complaints': complaints})

def handle_complaint(request, complaint_id, action):
    complaint = get_object_or_404(Complaint, id=complaint_id)
    
    if action == 'accept':
        complaint.status = 'Accepted'
        message = 'Your complaint has been accepted. We will address it as soon as possible.'
    elif action == 'reject':
        complaint.status = 'Rejected'
        message = 'Your complaint has been rejected. Please contact us for further information.'
    
    complaint.save()
    
    # Send email to the user
    send_mail(
        'Complaint Status Update',
        message,
        settings.DEFAULT_FROM_EMAIL,
        [complaint.email],
        fail_silently=False,
    )
    
    return redirect('complaint_list')

def status_buttons_view(request):
    return render(request, 'components/status_buttons.html')

def accepted_complaints_view(request):
    accepted_complaints = Complaint.objects.filter(status='Accepted')
    return render(request, 'components/accepted_complaints.html', {'complaints': accepted_complaints})

def solve_complaint(request, complaint_id):
    complaint = get_object_or_404(Complaint, id=complaint_id)
    complaint.status = 'Solved'
    complaint.save()
    
    # Send email to the user
    send_mail(
        'Complaint Solved',
        'Your complaint has been solved. Thank you for your patience.',
        settings.DEFAULT_FROM_EMAIL,
        [complaint.email],
        fail_silently=False,
    )
    
    return redirect('accepted_complaints')

def solved_complaints_view(request):
    solved_complaints = Complaint.objects.filter(status='Solved')
    return render(request, 'components/solved_complaints.html', {'complaints': solved_complaints})