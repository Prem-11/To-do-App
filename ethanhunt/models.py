from django.db import models
from django.contrib.auth.models import User, auth
# Create your models here.
class UserProfile(models.Model):
    agent_id=models.IntegerField()
    TodoTitle=models.CharField(max_length=100)
    TodoDesc=models.CharField(max_length=100)
    Category=models.CharField(max_length=100)
    DueDate=models.DateField()

    def __str__(self):
        return self.agent_id