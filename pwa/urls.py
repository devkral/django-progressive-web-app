from django.urls import path
from .views import Manifest, ServiceWorker, FetchJson

# Serve up serviceworker.js and manifest.json at the root
urlpatterns = [
    path('serviceworker.js', ServiceWorker.as_view()),
    path('manifest.json', Manifest.as_view()),
    path('fetch/json', FetchJson.as_view(), name="pwa_fetch_json"),
]
