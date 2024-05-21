from studentapp.models import Achivments
from studentapp.models import attandence
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
        model = attandence
        fields=['teacher_id','present']
        
