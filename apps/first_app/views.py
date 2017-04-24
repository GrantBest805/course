from django.shortcuts import render, redirect
from .models import Course

def index(request):
    context = {
    "courses": Course.objects.all()
    }

    return render(request, 'first_app/index.html', context)

def show(request):
    Course.objects.create(name=request.POST['name'], description=request.POST['description'])

    return redirect('/')

def remove(request, id=None):
    context = {
    "courses": Course.objects.filter(id=id)
    }


    return render(request, 'first_app/remove.html', context)

def clear(request, id):


    Course.objects.get(id=id).delete()

    return redirect('/')
