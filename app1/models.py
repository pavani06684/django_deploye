from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class employee(models.Model):
    employee_name=models.CharField(max_length=20)
    employee_id=models.IntegerField(unique=True,auto_created=True)
    employee_email=models.CharField(max_length=30)
    employee_salay=models.FloatField()