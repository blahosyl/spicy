from django.shortcuts import render, get_object_or_404, reverse
from .models import Profile



def all_profiles(request):
    """
    Renders the Profiles page, showing all profiles
    """
    # Retrieve and get all profiles from the database
    profiles = Profile.objects.all()

    # Render the profiles.html template with the profiles context
    return render(
        request,
        "community/profiles.html",
        {"profiles": profiles},
    )



def profile_detail(request, slug):
    """
    Display details of an individual profile.

    :param request: The HTTP request object.
    :param slug: The slug of the profile to display.

    **Context**

    ``profile``
        An instance of :model:`community.Profile`.

    **Template:**

    :template:`community/profile_detail.html`
    """

    # Retrieve and get all profiles from the database
    queryset = Profile.objects.all()

    # Get the specific profile based on the slug or return a 404 error
    profile = get_object_or_404(queryset, slug=slug)

    # Render the profile_detail.html template with the profile context
    return render(
        request,
        "community/profile_detail.html",
        {"profile": profile},
    )
