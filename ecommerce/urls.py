from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('loja/', include('loja.urls')),
    path('admin/', admin.site.urls),
]
