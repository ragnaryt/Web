
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pride/', include('pride.urls')),
    path('common/', include('common.urls')),
]
