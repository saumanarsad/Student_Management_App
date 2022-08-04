from django.shortcuts import render
from django.http import HttpResponse
from .models import Students
from django.template import loader
# Create your views here.

def index(request):
    mystudents = Students.objects.all().values()
    template = loader.get_template('index.html')
    context = {"mystudents": mystudents}
    return HttpResponse(template.render(context,request))

