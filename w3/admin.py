from django.contrib import admin
from w3.models import Student

# Register your models here.

@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
    list_display=['id','name','age','city']


