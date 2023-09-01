from django.shortcuts import render , redirect
from .models import *
from django.contrib.auth import login,logout,authenticate

def index(request):
    return render(request,'index.html')

def registration(request):
    error = ''
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        un = request.POST['uname']
        em = request.POST['email']
        pwd = request.POST['pwd']
        try:
            user = User.objects.create_user(first_name=fn,last_name=ln,username=em,password=pwd)
            EmployeeDetails.objects.create(user=user,uname=un)
            error="no"
        except:
            error="yes"

    return render(request,'registration.html',locals())


def user_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['emailid']
        p = request.POST['password']
        user = authenticate(username=u,password=p)
        if user:
            login(request, user)
            error = "no"
        else:
            error = "yes"
    return render(request,'user_login.html',locals())

def emp_home(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    return render(request,'emp_home.html')

def Logout(request):
    logout(request)
    return redirect('index')


def profile(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error = ''
    user = request.user
    employee = EmployeeDetails.objects.get(user=user)
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        un = request.POST['uname']
        contact = request.POST['contact']
        jdate = request.POST['jdate']
        gender = request.POST['gender']

        employee.user.first_name = fn
        employee.user.last_name = ln
        employee.uname = un
        employee.contact = contact
        employee.gender = gender

        if jdate:
            employee.joiningdate = jdate

        try:
            employee.save()
            employee.user.save()
            error="no"
        except:
            error="yes"

    return render(request,'profile.html',locals())

def admin_login(request):
    return render(request,'admin_login.html')

def change_password(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error = ''
    user = request.user
    if request.method == "POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']

        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error="no"
            else:
                error = "not"
        except:
            error="yes"

    return render(request,'change_password.html',locals())

def admin_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request,'admin_login.html',locals())

def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request,'admin_home.html')

def change_passwordadmin(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ''
    user = request.user
    if request.method == "POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']

        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error="no"
            else:
                error = "not"
        except:
            error="yes"

    return render(request,'change_passwordadmin.html',locals())

def all_employee(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    employee = EmployeeDetails.objects.all()
    return render(request,'all_employee.html',locals())

def chating(request):
    messages = Message.objects.all().order_by('timestamp')
    return render(request, 'chating.html', {'messages': messages})

def send_message(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(content=content)
    return redirect('chating')

def file_share(request):
    return render(request,'file_share.html')
