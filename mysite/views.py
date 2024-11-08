from django.http import HttpResponse
from django.shortcuts import render
from employees.models import employee

def home(request):
    employeess = employee.objects.all()
    context = {
        'employess' : employeess,
    }
    return render(request,'home.html',context)