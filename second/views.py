from django.shortcuts import render
from django.http import HttpResponse
from .forms import TeacherForm

# Create your views here.

def second_home(request):
	form = TeacherForm()
	data = {'form': form}
	return render(request, 'second_home.html', data)