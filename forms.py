from django import forms
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class OTPValidationForm(forms.Form):
    otp = forms.CharField(max_length=6)

from .models import Ashram ,Functionhall,Volunteer

class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Ashram
        fields = ['name', 'email', 'password', 'confirm_password']

class ALoginForm(forms.ModelForm):
    class Meta:
        model = Ashram
        fields = ['name', 'password']


class FRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    password = forms.CharField(widget=forms.PasswordInput())


    class Meta:
        model = Functionhall
        fields = ['name', 'email', 'password', 'confirm_password']

class FLoginForm(forms.ModelForm):
    class Meta:
        model = Functionhall
        fields = ['name', 'password']


class VRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    password = forms.CharField(widget=forms.PasswordInput())


    class Meta:
        model = Volunteer
        fields = ['name', 'email', 'password', 'confirm_password']

class VLoginForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['name', 'password']

class ComplaintForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    complaint = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

