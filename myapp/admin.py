from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentsModel(admin.ModelAdmin):
    list_display=['id','Name','Course','City']
