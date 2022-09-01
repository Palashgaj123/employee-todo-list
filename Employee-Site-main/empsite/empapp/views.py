from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Employee
import re


# Create your views here.
def home(request):
    return render(request,'home.html')

def dashboard(request):
    e=Employee.objects.all()
    content={}
    content['data']=e
    return render(request,'dashboard.html',content)

def add_emp(request):
    if request.method=="POST":
        ename=request.POST['ename']
        econtact=request.POST['econtact']
        eemail=request.POST['eemail']
        n=len(econtact)
        e=regex=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if n==10:
            if (re.fullmatch(regex,eemail)):
                b=Employee.objects.create(emp_name=ename,emp_contact=econtact,emp_email=eemail)
                b.save()
                return HttpResponseRedirect('/dashboard')
            else:
                 err_msg={}
                 err_msg['e']="Invalid Email_Id"
                 return render(request,'add_emp.html',err_msg)

        else:
            err_msg={}
            err_msg['m']="Invalid Mobile Number"
            return render(request,'add_emp.html',err_msg)

    else:
        return render(request,'add_emp.html')

def register(request):
    if request.method=="POST":
        fm=UserCreationForm(request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password1']
            u=User.objects.create_user(username=uname,password=upass,is_superuser=True,is_staff=True)
            u.save()
            return HttpResponseRedirect('/user_login')
            
    else:
        fm=UserCreationForm()
    return render(request,'registration.html',{'form':fm})

def user_login(request):
    if request.method=="POST":
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            u=authenticate(username=uname,password=upass)
            if u is not None:
                login(request,u)
                return HttpResponseRedirect('/dashboard/')
    else:
        fm=AuthenticationForm()

    return render(request,'user_login.html',{'form':fm})

def u_logout(request):
     logout(request)
     return HttpResponseRedirect('/')
