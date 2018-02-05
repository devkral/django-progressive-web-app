import django
from .views import Manifest, ServiceWorker

if django.VERSION[0] >= 2:
    from django.urls import path
    # Serve up serviceworker.js and manifest.json at the root
    urlpatterns = [
        path('serviceworker.js', ServiceWorker.as_view()),
        path('manifest.json', Manifest.as_view())
    ]
else:
    from django.conf.urls import url
    # Serve up serviceworker.js and manifest.json at the root
    urlpatterns = [
        url('serviceworker.js$', ServiceWorker.as_view()),
        url('manifest.json$', Manifest.as_view())
    ]
