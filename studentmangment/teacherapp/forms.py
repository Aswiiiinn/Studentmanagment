from .models import *
from django import forms

class courseForm(forms.ModelForm):
    class Meta:
        model = CourseMeterial
        fields = '__all__'