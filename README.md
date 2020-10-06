 #Django #Login #Register #Authentication


## from CMD on windows##

* my_django_app>python -m venv env

* my_django_app>env\Scripts\activate

* (env)  \my_django_app>pip install django

* (env)  \my_django_app>django-admin startproject my_django_app

* (env)  \my_django_app\my_django_app>python manage.py startapp hello (create another directory)

* * (in vscode)go to settings.py --> installed_apps --> add 'hello'

* (env)  \my_django_app\my_django_app>python manage.py runserver (it will run at http://127.0.0.1:8000/)

* * http://127.0.0.1:8000/admin gets admin panel page

* * @cmd Ctrl + c --> stop running 

* (env)  \my_django_app\my_django_app>python manage.py migrate (it will create a db)

* (env)  \my_django_app\my_django_app>python manage.py createsuperuser

* * (in vscode)go to /hello / view.py

	from django.shortcuts import render

	def  index(request):
    		return render(request,'hello/index.html')

     (in vscode) create templates / index.html

* * (env) \my_django_app\my_django_app> python manage.py startapp accounts

 >PS : For Python use cmd terminal in VSCode , for activating env (my_django_app>env\Scripts\activate)


"# CreateDjango" 

