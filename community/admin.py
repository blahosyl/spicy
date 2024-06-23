from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile



# Register and Creating the Profile model with the admin decorator function and using the ProfileAdmin class
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    # Automatically populate the 'slug' field based on the 'user' field
    prepopulated_fields = {"slug": ("user",)}

    # Restrict the queryset to allow only staff users (non-superadmins) to view, change, and delete their own profiles
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs  # Superusers can see all profiles
        return qs.filter(user=request.user)  # Staff users can only see their own profiles

    # Restrict the user selection in the admin form for staff users
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user" and not request.user.is_superuser:
            kwargs["queryset"] = User.objects.filter(username=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



