from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import MovieForm
from . models import Movie
# Create your views here.
def index(request):
    mve=Movie.objects.all()
    dict={
        'movie_list':mve
    }
    return render(request,"index.html",dict)
def detail(request,m_id):
    mve=Movie.objects.get(id=m_id)
    return render(request,"detail.html",{'dict':mve})

def add(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        img=request.FILES['img']
        movie=Movie(name=name,desc=desc,year=year,img=img)
        movie.save()
    return render(request,"edit.html")

def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"update.html",{'movie':movie,'form':form})

def delete(request,id):
    if request.method=="POST":
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,"delete.html")