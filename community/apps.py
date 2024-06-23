from django.apps import AppConfig

class CommunityConfig(AppConfig):
    # Default field type for auto-generated primary keys
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Name of the app
    name = 'community'
