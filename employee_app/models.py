from django.db import models

# Create your models here.


class Employee(models.Model):
    employee_no = models.CharField(max_length=10, unique=True)
    employee_name = models.CharField(max_length=100)
    email_id = models.EmailField()
    mobile_no = models.CharField(max_length=15)
    salary = models.IntegerField()

   