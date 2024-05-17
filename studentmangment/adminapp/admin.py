from django.contrib import admin
from studentapp.models import *
from .forms import *

class StudentAdmin(admin.ModelAdmin):
    list_display =['name','batch','course','score']
    list_editable=['name','batch','course','score']
# Register your models here.
