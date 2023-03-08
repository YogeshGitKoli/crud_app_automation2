from .forms import *
from django.shortcuts import render
from django.urls import reverse
from .models import Student
from django.contrib.auth import views as Auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView,TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView


class AllData(LoginRequiredMixin,ListView): 
    model=Student
    template_name='web/content/AllData.html'
    context_object_name='form'
    paginate_by=7

class AddData(SuccessMessageMixin,LoginRequiredMixin,CreateView):
    form_class=StudentForm
    template_name='web/content/AddData.html'
    context_object_name='form'
    success_url='/AddData/'
    success_message='Student Added Successfully!!!'


class UpdateData(SuccessMessageMixin,LoginRequiredMixin,UpdateView):
    model = Student
    form_class=StudentForm
    template_name='web/content/UpdateData.html'
    context_object_name='form'
    success_message='Student Update Successfully!!!'

    def get_success_url(self):
           pk = self.kwargs["pk"]
           return reverse("UpdateData", kwargs={"pk": pk})

class DeleteData(SuccessMessageMixin,LoginRequiredMixin,DeleteView):
    model=Student
    template_name='web/content/DeleteData.html'
    success_url='/AllData/'
    context_object_name='form'
    success_message='Deleted Successfully'


class SignUpUser(SuccessMessageMixin,CreateView):
    form_class=NewUserForm
    template_name='web/security/AddNewUser.html'
    success_url='/SignUp/'
    success_message='Your account has been created!!! Now you can login.'
    

class SignInUser(SuccessMessageMixin,Auth.LoginView):
    authentication_form=LoginUserForm
    template_name='web/security/LoginUser.html'
    success_url='/SignIn/'
    success_message='Welcome to CRUD Application'

class PasswordChangeUser(LoginRequiredMixin,SuccessMessageMixin,Auth.PasswordChangeView):
    form_class=PassChangeForm
    template_name='web/security/PassChangeUser.html'
    success_url='/PassChangeDone/'
    success_message='Your Password Changed Successfully!!!'
    login_url='/SignIn/' 

class PassChangeDoneUser(Auth.PasswordChangeDoneView):
    template_name='web/security/PassChangeUser.html'

class SignOutUser(Auth.LogoutView):
    template_name='web/security/LoginUser.html'