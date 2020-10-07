from django.contrib import admin
from .models import Term
# Register your models here.

class TermModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request): #disable add property @Term Admin Panel
        return False


    def  has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Term,TermModelAdmin)






# (env) \my_django_app\my_django_app>python manage.py makemigrations
#                                    python manage.py migrate (for create Term model in admin page)

# (env) \my_django_app\my_django_app>python manage.py makemigrations --empty Term (for creating empty migration file ,  Term\migrations\0002_auto_20201006_1620.py)