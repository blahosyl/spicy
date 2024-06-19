from django.contrib import admin
from .models import Profile
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(SummernoteModelAdmin):

    summernote_fields = ('about',)
