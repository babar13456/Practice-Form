from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('', include('first.urls')),
	path('second/', include('second.urls')),
    path('admin/', admin.site.urls),
]
