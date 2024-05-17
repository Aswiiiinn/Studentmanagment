from django.shortcuts import render,redirect
from django.views import View
from studentapp.models import Batch
from adminapp.forms import BatchForm

class viewbatch(View):
    def get(self,request):  
        item = Batch.objects.all()
        form = BatchForm()
        context = {'form': form, 'item': item}
        return render(request,'viewbatch.html',context)
    
class addbatch(View):
    def get(self,request):
        form = BatchForm()
        return render(request,'addbatch.html',{'form':form})
    def post(self,request):
        form = BatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('batchapp:batch_view')
        return render(request,'addbatch.html',{'form':form})
class updatebatch(View):
    def get(self,request,pk):
        item = Batch.objects.get(id=pk)
        form = BatchForm(instance=item)
        return render(request,'updatebatch.html',{'form':form})
    def post(self, request,pk): 
        item = Batch.objects.get(id=pk)
        form = BatchForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('batchapp:batch_view')
        return render(request,'updatebatch.html',{'form':form})

class delete(View):
    def get(self,request,pk):
        item = Batch.objects.get(id=pk)
        item.delete()
        return redirect('batchapp:batch_view')
    
# Create your views here.
