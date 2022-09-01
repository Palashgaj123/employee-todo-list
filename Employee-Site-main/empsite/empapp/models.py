from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_name=models.CharField(max_length=50)
    emp_contact=models.BigIntegerField()
    emp_email=models.EmailField(max_length=50)
