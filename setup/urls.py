
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')), # ponte para galeria.urls, onde as requisições serão direcionadas
    
    
]
