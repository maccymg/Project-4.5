from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/pictures/', include('pictures.urls')),
    path('api/types/', include('picture_types.urls')),
]
