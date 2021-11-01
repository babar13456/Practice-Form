from django.urls import path
from . import views

urlpatterns = [
	path('', views.second_home, name='second_home')
]
