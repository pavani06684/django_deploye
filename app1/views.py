from django.shortcuts import render
from app1.models import employee
# Create your views here.

def emp_details(request):
    data=employee.objects.all()
    context={
        'data':data
    }
    return render(request,'app1_Tem/home.html',context)