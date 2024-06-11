from datetime import date
import random
import string
from django.db.models import Q
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import login,logout,authenticate

from studentmangment import settings
from adminapp.models import notifications
from .models import Student, User,Teacher
from django.core.mail import send_mail
from django.http import  HttpResponse, HttpResponseBadRequest


def index(request):

    return render(request,'main.html')

class RedirecttoRegistration(View):
    def get(self,request):
        return render(request,'RedirecttoRegistration.html') 
    def post(self, request):
        user_type = request.POST.get('user_type')  # Assuming 'user_type' is a field in your form
        
        if user_type == 'admin':
            return redirect('Registraion1')
        # elif user_type == 'teacher':
        #     return redirect('Registraion2')
        if user_type == 'student':
           return redirect('Registraion3')
        else:
            # Handle invalid user type selection
            return HttpResponse('Invalid user type selected')
class Registraion1(View):
    def get(self,request):
        return render(request, 'Registraion1.html')
    def post(self,request):
        username = request.POST.get('username')
        passwordd = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            is_admin = True
            user = User.objects.create_user(username=username, password=passwordd)
            login(request,user)
            return redirect('admin_login')
        return render(request, 'Registraion1.html')
# class Registraion2(View):
#     def get(self,request):
#         return render(request, 'Registraion2.html')
#     def post(self,request):
#         username = request.POST.get('username')
#         passwordd = request.POST.get('password')
#         teacher_email = request.POST.get('teacher_email')

#         if not User.objects.filter(username=username).exists():
#             user = User.objects.create_user(username=username, password=passwordd,email=teacher_email )
#             login(request,user)
#             return redirect('home')
#         return render(request, 'Registraion2.html')
class Registraion3(View):
    def get(self,request):
        return render(request, 'Registraion3.html')
    def post(self,request):
        username = request.POST.get('username')
        passwordd = request.POST.get('password')
        student_email = request.POST.get('teacher_email')
        
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, password=passwordd,email=student_email )
            login(request,user)
            return redirect('home')
        return render(request, 'Registraion3.html')


class AdminLoginView(View):
    def get(self, request):
        return render(request, 'admin_login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_admin:
            login(request, user)
            return redirect('adminapp:dash')
        else:
            return HttpResponse('Invalid credentials or not an admin user')

class TeacherLoginView(View):
    def get(self, request):
        return render(request, 'teacher_login.html')

    def post(self, request):
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        print(password) 
        teacher_email = request.POST.get('email')
        print(teacher_email)
        user =Teacher.objects.filter(email= teacher_email,username=username,password=password).exists()
        print(user)
        if user:  
        
            return redirect('teacherapp:tchrdash')
        else:
           return HttpResponse('invalid')

class otp_email(View):
    def get(self, request):
        return render(request, 'otppageemail.html')

    def post(self, request):
        email = request.POST.get('email')
        
        otp = ''.join(random.choices( string.digits, k=4))
        print("hi:",otp)

        subject = "OTP!"
        message = f'This is your OTP: {otp}'
        from_email = settings.EMAIL_HOST_USER
        to_email = [email]
        send_mail(subject, message, from_email, to_email)

        request.session['otp'] = otp
        return redirect('otp_varification')  # Assuming 'otp_verification' is the URL name for OTP verification page

class otp_verification(View):
    def get(self, request):
        return render(request, 'otppage.html')

    def post(self, request):
        otp_entered = request.POST.get('otp')
        otp_generated = request.session.get('otp')
        if otp_entered == otp_generated:
            # Correct OTP entered
            return redirect("teacherapp:tchrdash")  # You can redirect to another page or return any message you want
        else:
            # Incorrect OTP entered
            return HttpResponse("Invalid OTP. Please try again.") 
    # def get(self,request):
    #     return render(request,'otppage.html')
    # def post(self,request):
    #     otp1 = request.POST.get('otp')
    #     otp =request.session.get('otp')
    #     if otp1==otp:
    #         return redirect('teacher_dashboard')
    #     else:
    #         return HttpResponse("wrong otp")
        
    

class StudentLoginView(View):
    def get(self, request):
        return render(request, 'student_login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        student_email = request.POST.get('email')
        print(student_email, password ,username )
        
        user = Student.objects.get(username=username, password=password,email=student_email)
        course = user.course
        batch = user.batch
        teacher = Teacher.objects.get(courses__name=course ,batches__name=batch)
        noti = notifications.objects.filter(Q(teacher=teacher)|Q(teacher__isnull=True))
        print(user) 
        reminders = []
        for notif in notifications:
            days = int((notif.expiry_date - date.today()).days)
            if 0 <= days <= 5:
                reminders.append((notif, days))
                print(reminders)
                return redirect('studentview')
            return render(request,'student_login.html',{'user':user, 'noti':notif, 'days':days})
class studentview(View):
    def get(self,request):
        return render(request,'studentview.html')
