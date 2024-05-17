import random
import string
from django.shortcuts import render,redirect
from studentapp.models import Student,Course,Batch,Teacher
from django.views import View
from django.core.mail import send_mail

from studentmangment import settings
from .forms import *
# Create your views here.
# cread operation for student
class dash(View):
    def get(self, request):
        return render(request,"main1.html")
    def post(self, request):
        user_type = request.POST.get('user_type')
        if user_type =="Edit_Student":
            return redirect('adminapp:index')
        if user_type == "Edit_Teacher":
            return redirect('teacherapp:teacher_view')
        if user_type == "Edit_Course":
            return redirect('courseapp:course_view')
        if user_type == "Edit_Batch":
            return redirect('batchapp:batch_view')
class Studentview(View):
    def get(self, request):
        item = Student.objects.all()
        forms = StudentForm()
        context ={'item':item, 'forms':forms}
        return render(request,"admindashbord.html", context)
class StudentAdd(View):
    def get(self, request):
        forms = StudentForm()
        return render(request,"studentadd.html",{'forms':forms})
    def post(self, request):
        forms = StudentForm(request.POST)
        if forms.is_valid():
            std = forms.save(commit=False)
            p=6
            password_is = ''.join(random.choices(string.digits,k=p))
            std.username = std.name
            std.password = password_is
            email = std.email
 
            forms.save()
            subject = "Student Password and Username"
            message = f"this is  Username\n{std.username}\tand Password\n{std.password}"
            from_email = settings.EMAIL_HOST_USER
            to_email  = [email]
            send_mail(subject, message, from_email, to_email)
            return redirect('adminapp:index')
        return render(request,"studentadd.html",{'forms':forms})
class UpdateStudent(View):
    def get (self,request,pk):
        item = Student.objects.get(id=pk)
        form = StudentForm(instance=item)
        return render(request,"updatestudent.html",{'form':form})
    def post(self, request,pk):
        item = Student.objects.get(id=pk)
        form = StudentForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('adminapp:index')
        return render(request,"updatestudent.html",{'form': form})

class DeleteStudent(View):
    def get(self, request, pk):
        try:
            # Retrieve the student object with the given pk
            item = Student.objects.get(id=pk)
        except Student.DoesNotExist:
            # Handle the case where the student does not exist
            # Redirect to a suitable URL or return an error response
            return redirect('adminapp:index')  # Redirect to a suitable URL

        # Delete the student object
        item.delete()

        # Redirect to a suitable URL after successful deletion
        return redirect('adminapp:index')  # Redirect to a suitable URL

        
    
