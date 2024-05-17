from django.shortcuts import render,redirect
from studentapp.models import Course
from django.views import View
from adminapp.forms import CourseForm

class viewCourse(View):
    def get(self,request):
        item = Course.objects.all()
        form = CourseForm()
        context = {'form': form, 'item': item}
        return render(request,'viewcourse.html',context)
class addcourse(View):
    def get(self,request):
        form = CourseForm()
        return render(request,'addcourse.html',{'form':form})   
    def post(self,request):
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courseapp:course_view')
        return render(request,'addcourse.html',{'form':form})
class updatecourse(View):
    def get(self,request,pk):
        item = Course.objects.get(id=pk)
        form = CourseForm(instance=item)
        return render(request,'updatecourse.html',{'form':form})
    def post(self,request,pk):
        item = Course.objects.get(id=pk)
        form = CourseForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('courseapp:course_view')
        return render(request,'updatecourse.html',{'form':form})
class delete(View):
    def get(self,request,pk):
        item = Course.objects.get(id=pk)
        item.delete()
        return redirect('courseapp:course_view')
# Create your views here.
