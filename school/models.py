from django.db import models
import datetime

# Create your models here.
class SchoolFee(models.Model):
    total_amount = models.DecimalField(max_digits=7, decimal_places=2, verbose_name = 'Total Amount')
    paid_amount = models.DecimalField(max_digits=7, decimal_places=2, verbose_name = 'Paid Amount')
    due_amount = models.DecimalField(max_digits=7, decimal_places=2, verbose_name = 'Due Amount')

class TransportFee(models.Model):
    total_amount = models.DecimalField(max_digits=7, decimal_places=2, verbose_name = 'Total Amount')
    paid_amount = models.DecimalField(max_digits=7, decimal_places=2, verbose_name = 'Paid Amount')
    due_amount = models.DecimalField(max_digits=7, decimal_places=2, verbose_name = 'Due Amount')

class Category(models.Model):
    category_name = models.CharField(max_length=30)

class Standard(models.Model):
    class_name = models.CharField(max_length=20)

class Student(models.Model):
    name = models.CharField(max_length=50)
    present_standard = models.ForeignKey('Standard', on_delete=models.CASCADE)

class StudClass(models.Model):
    stud_id = models.ForeignKey('Student', on_delete=models.CASCADE)
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE)

class Parent(models.Model):
    stud_id = models.ManyToManyField('Student')
    parent_name = models.CharField(max_length=50)
    relationship = models.CharField(max_length=50)

class StudentParentRelationship(models.Model):
    parent_id = models.ManyToManyField('Parent')
    stud_id = models.ManyToManyField('Student')

class SchoolFeeTransaction(models.Model):
    school_fee_id = models.ForeignKey('SchoolFee', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    date = models.DateField(default = datetime.date.today())

class TransportFeeTransaction(models.Model):
    transport_fee_id = models.ForeignKey('TransportFee', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    date = models.DateField(default = datetime.date.today())
