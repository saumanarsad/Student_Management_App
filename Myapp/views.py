from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Students
from django.template import loader
from django.urls import reverse
# Create your views here.

def index(request):
    mystudents = Students.objects.all().values()
    template = loader.get_template('index.html')
    context = {"mystudents": mystudents}
    return HttpResponse(template.render(context,request))

def add(request):
    template = loader.get_template('add.html')
    context = {}
    return HttpResponse(template.render(context,request))

def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    student = Students(firstname = x, lastname = y)
    student.save()
    return HttpResponseRedirect(reverse('index'))

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
    student.lastname =  last
    student.save()
    return HttpResponseRedirect(reverse('index'))
