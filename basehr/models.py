from __future__ import unicode_literals
from datetime import date
from django.utils.translation import gettext as _

from django.db import models

class Employee(models.Model):
    emp_id = models.AutoField(unique=True, primary_key=True)
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50, blank=True)
    lastname = models.CharField(max_length=50)
    gender = models.CharField(max_length=6)
    email = models.EmailField()
    blood_group = models.CharField(max_length=3)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=15, default='Karnataka')
    pincode = models.IntegerField()
    joining_date = models.DateField(_("Date"), default=date.today)
    marital_status = models.CharField(max_length=10)
    designation = models.CharField(max_length=30)
    emp_department = models.ForeignKey('Department')
    dob = models.DateField(verbose_name='Date of Birth')
    # reporting_to = models.ManyToManyField('self')
    comment = models.TextField()

    def __unicode__(self):
        return self.employee_name

class Department(models.Model):
    department_name = models.CharField(max_length=30)
    department_head = models.ForeignKey(Employee, blank=True)

    def __unicode__(self):
        return self.department_name

class PastEmployment(models.Model):
    emp_id = models.ForeignKey(Employee)
    past_employment_details = models.TextField()

    def __unicode__(self):
        return self.emp_id