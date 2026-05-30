from django.contrib import admin
from app1.models import employee
# Register your models here.

class employee_admin(admin.ModelAdmin):
    list_display=["employee_name","employee_id","employee_email","employee_salary"]
    ordering=["employee_id"]
admin.site.register(employee,employee_admin)