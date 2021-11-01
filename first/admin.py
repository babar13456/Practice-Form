from django.contrib import admin
from .models import *

# Register your models here.

class ListingAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'father_name', 'roll_no', 'address')
	search_fields = ('id', 'name', 'father_name', 'address')


admin.site.register(Student, ListingAdmin)