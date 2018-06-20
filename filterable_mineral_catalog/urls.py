from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from . import views

urlpatterns = [
    path('', include('minerals.urls', namespace='minerals')),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ]+urlpatterns
