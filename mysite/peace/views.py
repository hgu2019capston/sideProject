from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.contrib import messages
from .models import Applicant
from .forms import PostForm

import random, string

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            applicant = form.save()
            applicant.pwd = makeRandomString()
            applicant.generate()
            return result(request, applicant.pwd) 
    else:
        form = PostForm()

    return render(request, 'peace/form.html', {'form':form})


def makeRandomString():
    randomStream = ""
    for i in range(0,10):
        randomStream+=str(random.choice(string.ascii_letters))
    return randomStream

def result(request, user_pw):
    return HttpResponse("Saved Successfully!<br>This is your future password. You have to keep this with screen capture or something.<br>" + user_pw)
