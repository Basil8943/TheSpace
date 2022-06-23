from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import Task
from . forms import TodoForm
from  django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

# Create your views here.

class Tasklistview(ListView):
    model=Task
    template_name = "home.html"
    context_object_name = "work"

class Taskdetailview(DetailView):
    model=Task
    template_name = "detail.html"
    context_object_name = "work"

class Taskupdateview(UpdateView):
    model = Task
    template_name = "edit.html"
    context_object_name = "work"
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy("taskdetail",kwargs={'pk':self.object.id})

class Taskdeleteview(DeleteView):
    model = Task
    template_name = "delete.html"
    success_url = reverse_lazy("tasklist")


def index(request):
    work = Task.objects.all()
    if request.method=="POST":
        name=request.POST.get('name','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,"home.html",{'work':work})

# def detail(request):
#     work=Task.objects.all()
#     return render(request,"detail.html",{'work':work})

def delete(request,t_id):
    if request.method == 'POST':
        task=Task.objects.get(id=t_id)
        task.delete()
        return redirect('/')
    return render(request,"delete.html")

def update(request,id):
    task=Task.objects.get(id=id)
    form=TodoForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"update.html",{'task':task,'form':form})


