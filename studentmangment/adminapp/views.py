import random
import string
from turtle import right
from django.http import FileResponse, HttpResponse
from django.utils.dateparse import parse_date
from django.shortcuts import render,redirect
from studentapp.models import Student,Course,Batch,Teacher, attandence1
from django.views import View
from django.core.mail import send_mail
import io
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
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

        
class createattandencereportpdf(View):
    def get(self,request):
        
     return render(request,'attandencereportpdf.html')
    
    def post(self, request):
        start_date = parse_date(request.POST.get('start_date'))
        end_date = parse_date(request.POST.get('end_date'))
        teacher_name = request.POST.get('teacher_name')
        if start_date and end_date:
            if teacher_name:
                
                 attendance = attandence1.objects.filter(date__range=[start_date, end_date], teacher_id=teacher_name)
            else:
                 attendance = attandence1.objects.filter(date__range=[start_date, end_date])
            detailed =[]
            for att in attendance:
                detailed.append(
                    {
                        'name': att.teacher_id.name,
                        'date': att.date,   
                        'arrival_time': att.arrival_time,
                        'break_start': att.break_start,
                        'break_end': att.break_end,
                        'departure_time': att.departure_time,
                        'total_breaking_hours':att.total_breaking_hours
                     
                        
                    })
            request.session['detailed']=detailed
            if not attendance.exists():
              return HttpResponse('No attendance records found for the given date range and teacher')
            else:
              return render(request,'attandencereportpdf.html',{'attendance':attendance,'start_date':start_date,'end_date':end_date,'teacher_id':teacher_name})
            
class createstudentreportpdf(View):
    def get(self,request):
        return render(request,'studentreportpdf.html')  
    def post(self,request):
        student_name1 = request.POST.get('Student_name')
        student_name = Student.objects.filter(name=student_name1)
        student_details = []
        for student in student_name:
             student_details.append({
                'name': student.name,
                'course_name': student.course.name,
                'mark': student.score
                })
            # Store student details in session
        request.session['student_details'] = student_details
        return render(request, 'studentreportpdf.html', {'student_name': student_name})
class pdfgenstudentreportpdf(View):
    def get(self, request):
        details = request.session.get('detailed')
        buf = io.BytesIO()
        c =canvas.Canvas(buf, pagesize=letter)
        text =c.beginText(40,750)
        text.setFont('Helvetica',14)
        for std in  details:
            text.textLine(f"Name:{std['name']}")
            text.textLine(f"arrival_time:{std['arrival_time']}")
            text.textLine(f"student_name:{std['student_name']}")
            text.textLine(f"break_start:{std['break_start']}")
            text.textLine(f"total_breaking_hours:{std['total_breaking_hours']}")
        c.drawText(text)
        c.showPage()
        c.save()
        buf.seek(0)
        response = FileResponse(buf, as_attachment=True, filename='students.pdf')
        return response
        
class pdfgen(View):
    def get(self, request):
        student_details = request.session.get('student_details')
        
       
        buffer = io.BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)
        text = p.beginText(40, 750)  # Set initial position
        text.setFont('Helvetica', 14)

        for student in student_details:
            text.textLine(f"Name: {student['name']}")
            text.textLine(f"Course: {student['course_name']}")
            text.textLine(f"Mark: {student['mark']}")
            text.textLine("")  # Add empty line for spacing

        p.drawText(text)
        p.showPage()
        p.save()
        
        buffer.seek(0)
        response = FileResponse(buffer, as_attachment=True, filename='students_report.pdf')
        return response
class coursecomplitionreportpdf(View):

    def get(self, request,pk):
        student = Student.objects.get(id=pk )
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{student.name}_certificate.pdf"'
        p = canvas.Canvas(response, pagesize=letter)
        width, height = letter
        p.setFont("Helvetica", 12)
        # Draw the certificate content
        p.drawCentredString(width / 2.0, height - 100, "Certificate of Completion")
        p.setFont("Helvetica", 18)
        p.drawCentredString(width / 2.0, height - 150, f"This is to certify that")
        p.setFont("Helvetica-Bold", 20)
        p.drawCentredString(width / 2.0, height - 200, f"{student.name}")
        p.setFont("Helvetica", 18)
        p.drawCentredString(width / 2.0, height - 250, f"has successfully completed the course")
        p.setFont("Helvetica-Bold", 20)
        p.drawCentredString(width / 2.0, height - 300, f"{student.course.name}")
        p.setFont("Helvetica", 16)
        p.drawCentredString(width / 2.0, height - 450, "Congratulations!")
        # Add a border (optional)
        p.rect(30, 30, width - 60, height - 60)
        # Save the PDF file
        p.showPage()
        p.save()
        return response
class Announcement(View):
    def get(self, request):
        return render(request,'announcement.html')