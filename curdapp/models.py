from django.db import models

class StudentData(models.Model):
    task=models.CharField(max_length=100)
    description=models.CharField(max_length=150)
