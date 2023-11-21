from django.contrib import admin
from os import environ
from .models import Audio

class AudioAdmin(admin.ModelAdmin):
    list_display = 'name', 'explicit'

    prepopulated_fields = {"slug": ["name"]}

    def render_change_form(self, request, context, *args, **kwargs):
        self.change_form_template = 'admin/api/audio_change_form_with_frontend_link.html'
        context['frontend_url'] = environ["FRONTEND_URL"]
        return super().render_change_form(request, context, *args, **kwargs)



# Register your models here.
admin.site.register(Audio, AudioAdmin)