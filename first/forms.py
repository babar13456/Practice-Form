from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = '__all__'

		labels = {
		'name': "",
		'father_name': ""
		}

		widgets = {
            'name' :  forms.TextInput(attrs={'placeholder': 'Enter Your Name'}),
            'father_name' :  forms.TextInput(attrs={'placeholder': 'Enter Father Name'}),
            'address': forms.TextInput(attrs={'placeholder': "Enter Your Address"})
		}
