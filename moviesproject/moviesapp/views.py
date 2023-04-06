from django.http import HttpResponse
from django.shortcuts import render, redirect
from. models import Movies
from. forms import MovieForm


# Create your views here.
def index(request):
    movie=Movies.objects.all
    context={
        'movie_list':movie
    }

    return render(request,'index.html',context)
def detail(request,movies_id):
    movie= Movies.objects.get(id=movies_id)
    return render(request,"details.html",{'movie':movie})
def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']
        movie=Movies(name=name,desc=desc,year=year,img=img)
        movie.save()
    return render (request,'add.html')

def update(request,id):
    movies=Movies.objects.get(id=id)
    forms=MovieForm(request.POST or None, request.FILES,instance=movies)
    if forms.is_valid():
        forms.save()
        return redirect('/')
    return render(request,'edit.html',{'forms':forms,'movies':movies})

def delete(request,id):
    if request.method=='POST':
        movie=Movies.objects.get(id=id)
        movie.delete()
        return  redirect('/')
    return render(request,'delete.html')