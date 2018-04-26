from django.contrib import admin
from .models import SchoolFee, TransportFee, Category, Standard, Student, StudClass, Parent, StudentParentRelationship, SchoolFeeTransaction, TransportFeeTransaction
# Register your models here.

admin.site.register(SchoolFee)
admin.site.register(TransportFee)
admin.site.register(Category)
admin.site.register(Standard)
admin.site.register(Student)
admin.site.register(StudClass)
admin.site.register(Parent)
admin.site.register(StudentParentRelationship)
admin.site.register(SchoolFeeTransaction)
admin.site.register(TransportFeeTransaction)
