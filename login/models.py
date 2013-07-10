from django.db import models

class Login(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

    class Meta:
        db_table = u'login' 
