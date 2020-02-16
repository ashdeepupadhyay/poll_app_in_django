from django.shortcuts import render

# Create your views here.
def home(request):
    context={}
    return render(request,"polls/home.html",context)

def create(request):
    context={}
    return render(request,"polls/create.html",context)

def results(request,poll_id):
    context={}
    return render(request,"polls/results.html",context)

def vote(request,poll_id):
    context={}
    return render(request,"polls/vote.html",context)