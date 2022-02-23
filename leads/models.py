from django.db import models
#from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser


#User = get_user_model()

class User(AbstractUser):
    pass


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #first_name = models.CharField(max_length=100)
    #last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.user.email


class Lead(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)

    agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"