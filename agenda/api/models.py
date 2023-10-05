from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):

    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    phone=models.CharField(max_length=18)
    mobile=models.CharField(max_length=18)
    email=models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="users")



