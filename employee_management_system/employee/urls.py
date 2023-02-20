from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', employee_home, name="employee_home"),
    path('all-emp', all_emp, name="all_emp"),
    path('add-emp', add_emp, name="add_emp"),
    path('delete-emp', delete_emp, name="delete_emp"),
    path('filter-emp', filter_emp, name="filter_emp"),    
]
