# employee-management-system

Creating an employee management system using Python and the Django web framework involves several steps. Here's a high-level overview of the process:

1. Set up your development environment: You'll need to have Python and Django installed on your computer. You can install Python from the official website, and then install Django using pip (the Python package manager).

2. Create a new Django project: In a terminal or command prompt, use the "django-admin startproject" command to create a new Django project. This will create a new directory with some basic files and configurations.

3. Create a new Django app: A Django project can have multiple apps, which are like individual modules of functionality. You can use the "python manage.py startapp" command to create a new app within your project.

4. Define your models: In your app, define your models using Python classes that inherit from the "models.Model" class. These models will represent your data (such as employees, departments, and positions) and will be used to create database tables.

5. Set up your database: In your project's settings file, configure your database settings (such as the database type, name, user, and password). Then use the "python manage.py migrate" command to create the necessary tables in your database.

6. Create your views: Views are Python functions that handle requests and generate responses. Create views for each page or functionality of your employee management system.

7. Define your URLs: URLs map URLs to views, and can include variables that are passed to the views. Define your URLs using the "urls.py" files in your app and project.

8. Create your templates: Templates are HTML files that define the structure and layout of your pages. Create templates for each view, and use Django's templating language to fill in dynamic data.

9. Test and refine: Test your employee management system and make adjustments as necessary.

Packages needs to install - Python, django, djangorestframework, pillow, sqllite

Software to test REST APIs - Postman

## Create the project directory
mkdir Python-Django-Projects
cd Python-Django-Projects

## Create a virtual environment to isolate our package dependencies locally
python3 -m venv django_env
## Activate environment
source /Users/nik4u/miniconda3/bin/activate django_env  

## Install Django and Django REST framework into the virtual environment
pip install django

pip install djangorestframework

pip install markdown       # Markdown support for the browsable API.

pip install django-filter  # Filtering support
