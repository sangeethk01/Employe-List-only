from django.shortcuts import render, get_object_or_404
from employees.models import employee
from django.http import Http404,HttpResponse
# Create your views here.

def employee_details(request, pk):
    employe = get_object_or_404(employee, pk=pk)
    context = {
        'emplyee' : employe,
    }
    return render (request, 'employee_details.html',context)
        
    