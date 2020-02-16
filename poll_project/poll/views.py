from django.shortcuts import render,redirect

from .forms import CreatePollForm
from .models import Poll


# Create your views here.
def home(request):
    polls=Poll.objects.all()
    context={'polls':polls}
    return render(request,"polls/home.html",context)

def create(request):
    if request.method == "POST":
        form = CreatePollForm(request.POST)
        if form.is_valid():
            #print(form.cleaned_data['question'])#printing the validated data
            form.save()
            return redirect('home')
    else:
        form=CreatePollForm()

    context={
        'form':form
    }
    return render(request,"polls/create.html",context)

def results(request,poll_id):
    context={}
    return render(request,"polls/results.html",context)

def vote(request,poll_id):
    context={}
    return render(request,"polls/vote.html",context)