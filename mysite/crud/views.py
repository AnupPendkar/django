from django.shortcuts import render, redirect
from .models import Emp
from django.contrib import messages

# Create your views here.
def createView(req):
    return render(req, 'create.html')

def store(req):
    emp = Emp()
    emp.emp_name = req.POST.get('emp_name')
    emp.emp_email = req.POST.get('emp_email')
    emp.emp_mobile = req.POST.get('emp_mobile')
    emp.save()
    messages.success(req, 'Employee added successfully!')
    return redirect('/create')

def index(req):
    emp = Emp.objects.all()
    return render(req, 'index.html', {'emp':emp})