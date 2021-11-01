from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StudentForm
from .models import Student
from django.contrib import messages

# Create your views here.

def home_page(request):
	show_form = StudentForm()
	data = {'show_form': show_form}
	return render(request, 'index.html', data)

def save_form(request):
	if request.method == 'POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Data Added Successfully...")
			return redirect('student_list')
		else:
			return redirect('save_form')
	else:
		return HttpResponse("Something wrong")

def student_list(request):
	all_students = Student.objects.all()
	data = {'all_students': all_students}
	return render(request, 'list.html', data)


def student_delete(request, pk):
	get_student_id = Student.objects.get(id=pk)
	if request.method == 'POST':
		get_student_id.delete()
		messages.error(request, 'Student Deleted...')
		return redirect('student_list')
	data = {'get_student_id': get_student_id}
	return render(request, 'delete.html', data)

def student_update(request, pk):
	get_student_id = Student.objects.get(id=pk)
	show_form = StudentForm(instance=get_student_id)
	if request.method == 'POST':
		show_form = StudentForm(request.POST, instance=get_student_id)
		if show_form.is_valid():
			student_name = show_form.cleaned_data.get('name')
			show_form.save()
			messages.warning(request, f'Student Updated: {student_name}')
			return redirect('student_list')
	data = {'show_form': show_form}
	return render(request, 'student_update.html', data)





