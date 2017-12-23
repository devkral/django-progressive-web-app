from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView

from . import app_settings

class ServiceWorker(TemplateView):
    content_type = 'application/javascript'
    template_name = app_settings.PWA_SERVICE_WORKER_PATH

class Manifest(TemplateView):
    content_type = 'application/json'
    template_name = 'manifest.json'

    def get_context_data(self, **kwargs):
        for setting_name in dir(app_settings):
            if setting_name.startswith('PWA_'):
                kwargs[setting_name] = getattr(app_settings, setting_name)
        return super().get_context_data(**kwargs)
