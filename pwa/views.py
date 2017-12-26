from django.views.generic.base import TemplateView
from django.apps import apps
from django.http import Http404, HttpResponse
import json

from . import app_settings

class ServiceWorker(TemplateView):
    content_type = 'application/javascript'
    template_name = app_settings.PWA_SERVICE_WORKER_PATH

    def get_context_data(self, **kwargs):
        kwargs['PWA_APP_FETCH_URL'] = app_settings.PWA_APP_FETCH_URL
        return super().get_context_data(**kwargs)

class Manifest(TemplateView):
    content_type = 'application/json'
    template_name = 'manifest.json'

    def get_context_data(self, **kwargs):
        for setting_name in dir(app_settings):
            if setting_name.startswith('PWA_'):
                kwargs[setting_name] = getattr(app_settings, setting_name)
        return super().get_context_data(**kwargs)

class FetchJson(View):
    def post(self, *args, **kwargs):
        data = json.loads(self.request.body)
        query_results = {}
        for model_name, value in data.items():
            model = apps.get_model(app_label=model_name)
            if not hasattr(model, "process_pwa_query"): # extracts allowed data from query
                raise Http404("Model does not exist or is not suitable")
            objs = model.filter(**value.get("filter", {})).exclude(**value.get("exclude", {}))
            query_results[model_name] = model.process_pwa_query(objs, self.request)
        return HttpResponse(json.dumps(query_results), content_type='application/json')
