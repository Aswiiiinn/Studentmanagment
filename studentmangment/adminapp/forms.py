from studentapp.models import Student, Teacher, Course, Batch,importex
from django import forms

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
        
        
class importexportForm(forms.ModelForm):
    class Meta:
        model = importex
        fields = '__all__'
