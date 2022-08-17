from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Students
from django.template import loader
from django.urls import reverse
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.


# The homepage view where all the students will be listed

def index(request):
    mystudents = Students.objects.all().values()
    template = loader.get_template('index.html')
    context = {"mystudents": mystudents}
    return HttpResponse(template.render(context, request))

# View to call the add function and add.html file

def add(request):
    template = loader.get_template('add.html')
    context = {}
    return HttpResponse(template.render(context, request))

# view to add the student in the list


def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    student = Students(firstname=x, lastname=y)
    student.save()
    return HttpResponseRedirect(reverse('index'))

# View to delete the student record according to his id
def delete(request,id):
    student = Students.objects.get(id=id)
    student.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request,id):
    student = Students.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {'mystudent' : student}
    return HttpResponse(template.render(context,request))

def updaterecord(request,id):

    student = Students.objects.get(id=id)
    first = request.POST["first"]
    last = request.POST["last"]
    student.firstname = first
    student.lastname = last
    student.save()
    return HttpResponseRedirect(reverse('index'))

def register(request):
    template = loader.get_template('register.html')
    context = {}
    return HttpResponse(template.render(context,request))

def register_request(request):
    if request.method =="POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('login')

    form = NewUserForm
    return render(request=request,template_name="register.html",context={"register_form":form})

def login_request(request):
    if request.method=="POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.info(request,f"You are now logged in as {username}.")
                return redirect('index')
            else:
                messages.error(request,"Invalid username or password")
        else:
            messages.error(request,"Invalid username or password")
    form = AuthenticationForm()
    return render(request=request,template_name="login.html",context={"login_form":form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('login')
