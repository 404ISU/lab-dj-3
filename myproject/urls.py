from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('gallery/', include('gallery.urls')),
    path('cats/', include('cats.urls')),
]