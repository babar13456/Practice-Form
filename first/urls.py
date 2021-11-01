from django.urls import path
from . import views

urlpatterns = [
	path('', views.home_page, name='home_page'),
	path('save_form/', views.save_form, name='save_form'),
	path('student_list/', views.student_list, name='student_list'),
	path('student_delete/<str:pk>/', views.student_delete, name='student_delete'),
	path('student_update/<str:pk>/', views.student_update, name='student_update')
]
