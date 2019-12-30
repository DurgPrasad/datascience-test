from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def create_view(request):
    
    return render(request,'home.html')


def add(request):
    num1=int(request.POST['num'])
    num2=int(request.POST['num1'])
    result=num1+num2


    return render(request,'result.html',{'result':result})
    
