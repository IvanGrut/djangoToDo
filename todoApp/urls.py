from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import settings, views

urlpatterns = [
    url(r'^todos/', include('todos.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
