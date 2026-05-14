from django.contrib import admin
from .models import Bark

# Register Bark model in the admin
@admin.register(Bark) # decorator to avoid implement "admin.site.register(Bark, BarkAdmin)"
class BarkAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'created_at') # to display these columns



