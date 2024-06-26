from django.db import models
from django.contrib.auth.models import User


# Create your models here.

from django.db import models


class Profile(models.Model):
    """
    A model for user profiles, related to but distinct from the User model
    """
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

    class Meta:
        """
        order from most to least recently updated
        """
        ordering = ["-updated_on"]

    def __str__(self):
        """
        How instances of this model are shown in the admin panel
        """
        return "username: " + self.user.username + " | first name: "\
            + self.firstname
