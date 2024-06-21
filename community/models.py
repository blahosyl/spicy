from django.db import models
from django.contrib.auth.models import User


# Create your models here.

from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile"
    )
    slug = models.SlugField(max_length=200, unique=True)
    firstname = models.CharField(max_length=200, blank=True)
    lastname = models.CharField(max_length=200, blank=True)
    pronouns = models.CharField(max_length=200, blank=True)
    neurodivergence = models.CharField(max_length=200, blank=True)
    about = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "username: " + self.user.username + " | first name: "
        + self.firstname
