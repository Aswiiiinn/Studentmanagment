from studentapp.models import Student, Teacher, Course, Batch,importex
from django import forms

from .models import *

class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields =  ['name', 'batch', 'course', 'score','email']
        
class TeacherForm(forms.ModelForm):
    
    class Meta:
        model = Teacher
        fields = ['name', 'batches', 'courses','email']
        
class CourseForm(forms.ModelForm):
    
    class Meta:
        model = Course
        fields = '__all__'

class BatchForm(forms.ModelForm):
    
    class Meta:
        model = Batch
        fields = '__all__'
class importForm(forms.Form):
    file = forms.FileField()
class AnnouncementForm(forms.ModelForm):
    class Meta:
        model  = announcment
        fields = '__all__'
class notificationForm(forms.ModelForm):
    class Meta:
        model  = notifications
        fields = '__all__'

    
    
        
