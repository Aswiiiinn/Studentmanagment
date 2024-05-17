import random
import string
from django.shortcuts import render,redirect
from studentapp.models import Teacher
from adminapp.forms import TeacherForm
from django.core.mail import send_mail
from django.views import View
from .models import *
from studentapp.models import *
from adminapp.forms import *
from . forms import *
from studentmangment import settings

class choose(View):
    def get(self,request):
        return render(request,'teacherdash.html')
    def post(self,request):
        name  = request.POST.get('action')
        if name == "Add_Course_Material":
            return redirect('teacherapp:addMeterial')

class viewteacher(View):
    def get(self,request):
        item = Teacher.objects.all()
        form = TeacherForm()
        
        context = {'form': form, 'item': item}
        return render(request,'teacherview.html',context)
class addteacher(View):
    def get(self,request):
        form = TeacherForm()
        return render(request,'addteacher.html',{'form':form})
    def post(self,request):
        form = TeacherForm(request.POST)
        
        if form.is_valid():
            teacher =form.save(commit=False)
            passwordlength = 6
            random_password =''.join(random.choices(string.ascii_letters+string.digits,k=passwordlength))
            
            teacher.username = teacher.name
            teacher.password =random_password
            email = teacher.email
            
            subject  = 'your account Info'
            message =f'hello this is your username\n: {teacher.username}\n this is your password\n:{teacher.password}'
            from_email =settings.EMAIL_HOST_USER
            to_email = [email]
            send_mail(subject,message,from_email,to_email)
            teacher.save()
            
            
            return redirect('teacherapp:teacher_view')
        return render(request,'addteacher.html',{'form':form})
class updateteacher(View):
    def get(self,request,pk):
        item = Teacher.objects.get(id=pk)
        form = TeacherForm(instance=item)
        # item2 = Teacher.objects.filter(batches__name='A').annotate(scores = Max('teacher__student_score'))
        # for teacher in item2:
        #     print(teacher.name)
        #     for batch in teacher.batches.all():
        #      print(batch.start_date)
        #      print(batch.end_date)

    
        return render(request,'updateteacher.html',{'form':form})
    
    def post(self,request,pk):
        item = Teacher.objects.get(id=pk)
        form = TeacherForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('teacherapp:teacher_view')
        return render(request,'updateteacher.html',{'form':form})
class delete(View):
    def get(self,request,pk):
        item = Teacher.objects.get(id=pk)
        item.delete()
        return redirect('teacherapp:teacher_view')
class addMeterial(View):
    def get (self,request):
        form = courseForm()
        return render(request,'addmeterial.html',{'form':form})
    
    def post(self,request):
        form = courseForm(request.POST,request.FILES)

        if form.is_valid():
            meterial_instance = form.save(commit=False)
            meterial_instance.save()
            return redirect('teacherapp:meterial_view')
        return render(request,'addmeterial.html',{'form':form})
class tchrdash(View):
    def get(self,request):
        return render(request,'teacherdash.html')
    
class meterialview(View):
    def get(self,request):
        item  = CourseMeterial.objects.all()
        form = courseForm()
        context = {'form': form, 'item': item}
        return render(request,'meterialview.html',context)
class deleteview(View):
    def get(self,request,pk):
        item = CourseMeterial.objects.get(id=pk)
        item.delete()
        return redirect('teacherapp:meterial_view')
class exceldownload(View):
    def get(self,request):
        item = importex.objects.all()
        form = importexportForm()
        return redirect(request,'exceldownload.html'{'form': form, 'item': item})
    def post(self,request):
        student = importex.objects.