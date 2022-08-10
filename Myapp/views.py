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
