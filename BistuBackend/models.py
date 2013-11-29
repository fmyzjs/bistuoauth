# Create your models here.
from oauth2_provider.models import AbstractApplication
import hashlib
from django.db import models


class MyApplication(AbstractApplication):
    """
    Custom Application model which adds description field
    """
    description = models.TextField(blank=True)

class Account(models.Model):
    id=models.IntegerField(primary_key=True)
    userid = models.CharField(max_length=10)
    MasPass = models.CharField(max_length=32)
    username = models.CharField(max_length=20)
    idtype = models.IntegerField(max_length=1)

    def __unicode__(self):
        return self.username

    def is_authenticated(self):
        return True

    def hashed_password(self, password=None):
        if not password:
            return self.MasPass
        else:
            return hashlib.md5(password).hexdigest()
        
    def check_password(self, password):
        if self.hashed_password(password) == self.MasPass:
            return True
        return False
    
    class Meta:
        db_table = "member"
        app_label = 'bistu_member'