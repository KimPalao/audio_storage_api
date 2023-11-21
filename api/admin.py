from django.contrib import admin

from .models import Audio

class AudioAdmin(admin.ModelAdmin):
    list_display = 'name', 'explicit'

    prepopulated_fields = {"slug": ["name"]}


# Register your models here.
admin.site.register(Audio, AudioAdmin)