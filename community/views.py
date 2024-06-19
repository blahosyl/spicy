from django.shortcuts import render
from .models import Profile

# Create your views here.

def all_profiles(request):
    """
    Renders the Profiles page
    """
    profiles = Profile.objects.all()

    return render(
        request,
        "community/profiles.html",
        {"profiles": profiles},
    )