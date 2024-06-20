from django.shortcuts import render, get_object_or_404, reverse
from .models import Profile

def all_profiles(request):
    """
    Renders the Profiles page, showing all profiles
    """
    profiles = Profile.objects.all()

    return render(
        request,
        "community/profiles.html",
        {"profiles": profiles},
    )

def profile_detail(request, slug):
    """
    Display an individual :model:`community.Profile`.

    **Context**

    ``profile``
        An instance of :model:`community.Profile`.

    **Template:**

    :template:`community/profile_detail.html`
    """

    queryset = Profile.objects.all()
    profile = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "community/profile_detail.html",
        {"profile": profile,
        },
    )