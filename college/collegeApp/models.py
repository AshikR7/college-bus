from django.db import models

# Create your models here.
class busModel(models.Model):
    busNo=models.CharField(max_length=30)

class mailModel(models.Model):
    mail=models.EmailField()

class morning(models.Model):
    busNo=models.CharField(max_length=30)
    morg=models.CharField(max_length=10)
    time=models.DateTimeField(auto_now_add=True)

class evening(models.Model):
    busNo=models.CharField(max_length=30)
    even=models.CharField(max_length=10)
    time = models.DateTimeField(auto_now_add=True)