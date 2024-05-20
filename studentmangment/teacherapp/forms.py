from studentapp.models import Achivments
from .models import *
from django import forms

class courseForm(forms.ModelForm):
    class Meta:
        model = CourseMeterial
        fields = '__all__'
class achivmentForm(forms.ModelForm):
    class Meta:
        modles = Achivments
        fields = ['','score']