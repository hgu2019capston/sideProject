from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.contrib import messages
from .models import Applicant
from .forms import PostForm


def index(request):
    return HttpResponse("Hello")

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            applicant = form.save()
            applicant.generate()
            return redirect('index')
      
    else:
        form = PostForm()

    return render(request, 'peace/form.html', {'form':form})

