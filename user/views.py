
from typing import Any
from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import User
from .forms import ManagerRegistrationForm, DeveloperRegistrationForm
#import settings.py
from django.conf import settings
#send_mail is built-in function in django
from django.core.mail import send_mail
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.views import LoginView
from django.views.generic import ListView
from project.models import Project




# Create your views here.
class ManagerRegisterView(CreateView):
    template_name = 'user/manage_register.html'
    model = User
    form_class = ManagerRegistrationForm
    success_url = '/user/login/'
    
    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        #print("email....",email)
        if sendMail(email):
            print("Mail sent successfully")
            return super().form_valid(form)
        else:
            return super().form_valid(form)


class DeveloperRegisterView(CreateView):
    template_name = 'user/developer_register.html'
    model = User
    form_class = DeveloperRegistrationForm
    success_url = '/user/login/'  


def sendMail(to):
    subject = 'Welcome to PMS24'
    message = 'Hope you are enjoying your Django Tutorials'
    #recepientList = ["samir.vithlani83955@gmail.com"]
    recepientList = [to]
    EMAIL_FROM = settings.EMAIL_HOST_USER
    send_mail(subject,message, EMAIL_FROM, recepientList)
    #attach file
    #html
    return True


class UserLoginView(LoginView): 
    template_name = 'user/login.html'
    model = User
    
    
    def get_redirect_url(self):
        print(self.request.user)
        if self.request.user.is_authenticated:
            if self.request.user.is_manager:
                return '/user/manager-dashboard/'
            else:
                return '/user/developer-dashboard/'



class ManagerDashboardView(ListView):
    
    def get(self, request, *args, **kwargs):
        #logic to get all the projects
        print("ManagerDashboardView")
        projects = Project.objects.all() #select * from project
        print(".............................................",projects)
        
        return render(request, 'user/manager_dashboard.html',{
            "projects":projects
        })
    
    
    template_name = 'user/manager_dashboard.html'

#@MethodDecorator(loginDecorator)

class DeveloperDashboardView(ListView):
    def get(self, request, *args, **kwargs):
        #logic to get all the projects
        #loggedin developer --
        #select * from user_task where user_id = request.user.id
        #tasks = user_task.objects.filter(user=request.user)
        return render(request, 'user/developer_dashboard.html')
    
    template_name = 'user/developer_dashboard.html'    



    
       