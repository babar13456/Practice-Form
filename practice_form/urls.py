from django.contrib import admin
from django.urls import path, include

# This belongs to urls file.

urlpatterns = [
	path('', include('first.urls')),
	path('second/', include('second.urls')),
    path('admin/', admin.site.urls),
]
