from django.shortcuts import render
from helpdesk.models import help

def helprequest(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        concern=request.POST.get('concern')
        en=help(name=name,email=email,concern=concern)
        en.save()
        return render(request,'index.html')
# Create your views here.
