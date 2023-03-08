from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['Name','Course','City']

        widgets={
            'Name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Student Name'}),
            'Course':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Course Name'}),
            'City':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter City Name'}),
        }



"""SECURITY SECTION"""
#Create New User (Register) form of the user
class NewUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email']

        widgets={
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),

            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}),
        }

    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'New Password'}),label='Create Password')

    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Retype Password'}),label='Retype Password')

#Authenticate(Login) form of the user
class LoginUserForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Username','autofocus': True}),)

    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter The Password','autofocus': True}))

#password change form of the user
class PassChangeForm(PasswordChangeForm):
    old_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Old Password'}))

    new_password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter New Password'}),label='New Password')

    new_password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'RE-Enter New Password'}),label='Confirm Password')