from django.db import models
import datetime

# Create your models here.
class SchoolFee(models.Model):
    total_amount = models.DecimalField(max_digits=7, decimal_places=2, verbose_name = 'Total Amount')
    paid_amount = models.DecimalField(max_digits=7, decimal_places=2, verbose_name = 'Paid Amount')
    due_amount = models.DecimalField(max_digits=7, decimal_places=2, verbose_name = 'Due Amount')

    def __str__(self):
        return 'ID:%s, Total Amount:%s' %(self.id, self.total_amount)

class TransportFee(models.Model):
    total_amount = models.DecimalField(max_digits=7, decimal_places=2, verbose_name = 'Total Amount')
    paid_amount = models.DecimalField(max_digits=7, decimal_places=2, verbose_name = 'Paid Amount')
    due_amount = models.DecimalField(max_digits=7, decimal_places=2, verbose_name = 'Due Amount')

    def __str__(self):
        return 'ID:%s, Total Amount:%s' %(self.id, self.total_amount)

class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return 'ID:%s, Category:%s' %(self.id, self.category_name)

class Standard(models.Model):
    class_name = models.CharField(max_length=20)

    def __str__(self):
        return 'ID:%s, Standard:%s' %(self.id, self.class_name)

class Student(models.Model):
    name = models.CharField(max_length=50)
    present_standard = models.ForeignKey(Standard, on_delete=models.CASCADE)

    def __str__(self):
        return 'ID:%s, Name:%s, Present Standard:%s' %(self.id, self.name, self.present_standard)

class StudClass(models.Model):
    stud_id = models.ForeignKey('Student', on_delete=models.CASCADE)
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE)
    class_id = models.ForeignKey('Standard', on_delete=models.CASCADE)
    school_fee_id = models.ForeignKey('SchoolFee', on_delete=models.CASCADE)
    transport_fee_id = models.ForeignKey('TransportFee', on_delete=models.CASCADE)
    year = models.IntegerField()

    def __str__(self):
        return 'ID:%s, stud_id:%s, cateogry_id:%s, class_id:%s, school_fee_id:%s, transport_fee_id:%s, year:%s' %(self.id, self.stud_id, self.category_id, self.class_id, self.school_fee_id, self.transport_fee_id, self.year)

class Parent(models.Model):
    stud_id = models.ManyToManyField('Student')
    parent_name = models.CharField(max_length=50)

    def __str__(self):
        return 'ID:%s, stud_id:%s, Parent Name:%s' %(self.id, self.stud_id, self.parent_name)

class StudentParentRelationship(models.Model):
    parent_id = models.ManyToManyField('Parent')
    stud_id = models.ManyToManyField('Student')
    relationship = models.CharField(max_length=50)

    def __str__(self):
        return 'ID:%s, parent_id:%s, stud_id:%s, Relationship:%s' %(self.id, self.parent_id, self.stud_id, self.relationship)


class SchoolFeeTransaction(models.Model):
    reciept_number = models.IntegerField(unique=True)
    school_fee_id = models.ForeignKey('SchoolFee', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    date = models.DateField(default = datetime.date.today())

    def __str__(self):
        return 'ID:%s, school_fee_id:%s, Amount:%s, Date:%s' %(self.id, self.school_fee_id, self.amount, self.date)

class TransportFeeTransaction(models.Model):
    reciept_number = models.IntegerField(unique=True)
    transport_fee_id = models.ForeignKey('TransportFee', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    date = models.DateField(default = datetime.date.today())

    def __str__(self):
        return 'ID:%s, transport_fee_id:%s, Amount:%s, Date:%s' %(self.id, self.transport_fee_id, self.amount, self.date)
