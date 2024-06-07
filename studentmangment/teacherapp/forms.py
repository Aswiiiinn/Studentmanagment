from studentapp.models import Achivments
from studentapp.models import attandence1
from .models import *
from django import forms

class courseForm(forms.ModelForm):
    class Meta:
        model = CourseMeterial
        fields = '__all__'
class achivmentForm(forms.ModelForm):
    class Meta:
        model = Achivments
        fields = ['name','score']
class attandenceForm(forms.ModelForm):
    class Meta:
        model = attandence1
        fields=['teacher_id','present','present', 'arrival_time', 'break_start', 'break_end','departure_time']
        
