from django.db import models

class Student(models.Model):
    Name=models.CharField(max_length=50)
    Course=models.CharField(max_length=50)
    City=models.CharField(max_length=50)

    def __str__(self):
        return self.Name