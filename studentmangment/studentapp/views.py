from datetime import date
import random
import string
from django.http import JsonResponse
from django.db.models import Q
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import login,logout,authenticate
from .forms import *
from studentmangment import settings
from adminapp.models import notifications
from .models import Batch, Course, Student, User,Teacher, imageuploder1
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
        if user is not None:  
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
        form1 = FormWithCaptcha()
        return render(request, 'student_login.html',{'form1':form1})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = Student.objects.get(username=username, password=password)
        request.session['user_id'] = user.id
        request.session['user_name'] = user.name
        request.session['course'] = user.course.id
        request.session['batch'] = user.batch.id
        request.session['score'] = user.score
        return redirect('studentview')
        
class studentview(View):
    def get(self,request):
        user1=request.session.get('user')
        user = request.session.get('user_id')
        batch_id= request.session.get('batch')
        course_id = request.session.get('course')
        score =  request.session.get('score')
        user_name = (request.session.get('user_name','')).upper()   
        batch = Batch.objects.get(id=batch_id)
        course = Course.objects.get(id=course_id)
        item = imageuploder1.objects.get(student_id=user)
        teacher = Teacher.objects.filter(courses=course ,batches=batch)
        for teacher in teacher:
            print(f"Teacher: {teacher.name}")
            print("Teacher's Courses:")
            teacher_name = teacher.name
            for c in teacher.courses.all():
                print(c.name)
            print("Teacher's Batches:")
            for b in teacher.batches.all():
                print(b.name)
        
        noti = notifications.objects.filter(
                    Q(teacher_name_id=teacher.id) | Q(teacher_name__isnull=True))
        print(user) 
        reminders = []
        for notif in noti:
            days = int((notif.expire_date - date.today()).days)
            if 0 <= days <= 5:
                reminders.append((notif, days))
                print(reminders)
                # return redirect('studentview')
        return render(request,'studentmain.html',{'user1':user1,'user':user,'noti':noti,'reminders':reminders,'days':days,'score':score,'user_name':user_name,'course':course,'batch':batch,'item':item})
    
class imageviewer(View):
    def get(self, request):
        item = imageuploder1.objects.all()
        froms = imageForm()
        return render(request,'studentmain.html',{'item':item,'forms':froms})
class imageadder(View):
    def get(self,request):
        form = imageForm()
        return render(request,'imageadder.html',{'form':form})
    def post(self,request):
        form = imageForm(request.POST,request.FILES)
        if form.is_valid():
            forms.save()
            return redirect('studentview')
        return  render(request, 'imageadder.html',{'form':form})
class imageeditor(View):
    def get(self,request,pk):
        item = imageuploder1.objects.get(id=pk)
        form = imageForm(instance = item)
        return render(request,'imageeditor.html',{'item':item,'form':form})
    def post(self,request,pk):
        item = imageuploder1.objects.get(id=pk)
        form = imageForm(request.POST,request.FILES,instance = item)
        if form.is_valid():
            form.save()
            return redirect('studentview')
        return render(request,'imageeditor.html',{'item':item,'form':form})
class imagedelete(View):
    def get(self,request,pk):
        item = imageuploder1.objects.get(id=pk)
        item.delete()
        return redirect('studentview')
# class dropdadd(View):
#     def get(self,request):
#         form = dropdwonForm()
#         return render(request,'dropdwon.html',{'form':form})
#     def post(self,request):
        
#         form = dropdwonForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('dropdadd')
#         return render(request,'dropdwon.html',{'form':form})
# class updatedrop(View):
#     def get(self,request,pk):
#         item = student_detail.objects.get(id=pk)
#         form =dropdwonForm(instance=item)
#         return render(request,'updatedrop.html',{'form':form})
#     def post(self,request,pk):
#         item = student_detail.objects.get(id=pk)
#         form = dropdwonForm(request.POST,instance=item)
#         if form.is_valid():
#             form.save()
#             return redirect('dropdadd')
#         return render(request,'updatedrop.html',{'form':form})



class GetStatesView(View):
    def get(self, request):
        country_id = request.GET.get('country_id')
        states = State.objects.filter(country_id=country_id).values('id', 'name')
        return JsonResponse(list(states), safe=False)

class GetCitiesView(View):
    def get(self, request):
        state_id = request.GET.get('state_id')
        cities = City.objects.filter(state_id=state_id).values('id', 'name')
        return JsonResponse(list(cities), safe=False)

class StudentDetailView(View):
    def get(self, request):
        countries = Country.objects.all()
        form = StudentDetailForm()
        return render(request, 'ajaxtemp.html', {'countries': countries,'form': form})
# class djangocaptchaView(View):
#     def get(self, request):
       
#         print(form1)
#         return render(request, 'student_login.html', {'form1': form1})