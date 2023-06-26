from django.shortcuts import render, redirect
from . models import task
from . forms import todoforms

# Create your views here.
def function(request):
   tasks1=task.objects.all()
   if request.method=='POST':
      name=request.POST.get('task','')
      priority = request.POST.get('priority', '')
      date = request.POST.get('date', '')
      task2=task(name=name,priority=priority,date=date)
      task2.save()


   return render(request,'index.html',{'tasks1':tasks1})

def delete(request,taskid):
   task3=task.objects.get(id=taskid)
   if request.method=='POST':
      task3.delete()
      return redirect('/')
   return render(request,'delete.html')

def update(request,id):
   task4=task.objects.get(id=id)
   form1=todoforms(request.POST or None, instance=task4 )
   if form1.is_valid():
      form1.save()
      return redirect('/')
   return render(request,'edit.html',{'form1':form1,'task4':task4})
