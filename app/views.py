from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

def hello(request):
    tasks = Tasks.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'tasks':tasks,'forms': form}
    return render(request,'tasks/lists.html',context)



def updateTask(request,pk):
    taksform = Tasks.objects.get(id=pk)
    forms = TaskForm(instance=taksform)

    if request.method == 'POST':
        form = TaskForm(request.POST,instance=taksform)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': forms}
    return render(request,'tasks/update.html',context)


def delete(request, pk):
    item = Tasks.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item':item}
    return render(request,'tasks/delete.html',context)