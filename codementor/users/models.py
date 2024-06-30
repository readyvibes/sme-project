from django.db import models

# Create your models here.

class User(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(max_length=15, blank=True, default='')
    first_name = models.CharField(max_length=15, blank=True, default='')
    last_name = models.CharField(max_length=15, blank=True, default='')
    email = models.CharField(max_length=100, blank=True, default='')
    password = models.CharField(max_length=128) 
    class Meta:
        ordering = ['id']