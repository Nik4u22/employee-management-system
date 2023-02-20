from django.shortcuts import render
from django.db.models import Q
from .models import *
from datetime import datetime, timedelta

# Create your views here.
def employee_home(request):
    return render(request, 'employee_home.html', {})

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'employees': emps
    }
    return render(request, 'all_emp.html', context)

def add_emp(request):
    
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        dept_id = request.POST.get("department")
        department = Department.objects.get(pk=dept_id)
        salary = request.POST.get("salary")
        bonus = request.POST.get("bonus")
        role_id = request.POST.get("role")
        role = Role.objects.get(pk=role_id)
        phone = request.POST.get("phone")
        hire_date = request.POST.get("hire_date")
        
        employee = Employee()
        employee.first_name = first_name
        employee.last_name = last_name
        employee.dept = department
        employee.salary = salary
        employee.bonus = bonus
        employee.role = role
        employee.phone = phone
        employee.hire_date = datetime.strptime(hire_date, "%d-%m-%Y")
        employee.save()
        
    depts = Department.objects.all()
    roles = Role.objects.all()
    context = {
        'departments' : depts,
        'roles': roles
    }
    return render(request, 'add_emp.html', context)

def delete_emp(request):
    return render(request, 'delete_emp.html', {})

def filter_emp(request):
    
    emps = Employee.objects.all()
    
    if request.method == "POST":
        name = request.POST.get("first_name")
        department = request.POST.get("department")
        role = request.POST.get("role")

        emps2 = Employee.objects.all()
        print(emps2)
        if name:
            emps2 = emps2.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if department:
            emps2 = emps2.filter(dept__name__icontains = department)
        if role:
            emps2 = emps2.filter(role__name__icontains = role)

        depts = Department.objects.all()
        roles = Role.objects.all()
        context = {
            'departments' : depts,
            'roles': roles,
            'employees': emps2
        }
        print(emps2)
        return render(request, 'filter_emp.html', context)
        
    depts = Department.objects.all()
    roles = Role.objects.all()
    context = {
        'departments' : depts,
        'roles': roles,
        'employees': emps
    }
    
    return render(request, 'filter_emp.html', context)