from django.shortcuts import render,redirect
from django.contrib.auth import logout
from .models import newPost
from .forms import CrearPost

def crearPost(request):    
    if request.method == 'GET':
        form = CrearPost()
        context = {
                'form':form
            }
    elif request.method == 'POST':
        form = CrearPost(request.POST)
        context = {
                'form':form
            }
        if form.is_valid:
            form.save()
            return redirect('')

    return render(request, 'crearPost.html', context)

# Create your views here.
