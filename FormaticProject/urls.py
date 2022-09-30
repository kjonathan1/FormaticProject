from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from invoiceApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('invoice/', include('invoiceApp.urls')),
    path('training/', include('training.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
