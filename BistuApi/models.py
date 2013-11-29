from django.db import models

# Create your models here.

class Student(models.Model):
    
    id=models.IntegerField(primary_key=True)
    username = models.CharField(max_length=20)
    userid = models.CharField(max_length=10)
    idtype = models.IntegerField(max_length=1)
    


    class Meta:
        ordering = ('userid',)
        db_table = 'member'
        app_label = 'bistu_member'