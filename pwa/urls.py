from django.urls import path
from .views import manifest, service_worker

# Serve up serviceworker.js and manifest.json at the root
urlpatterns = [
    path('serviceworker.js', service_worker),
    path('manifest.json', manifest)
]
