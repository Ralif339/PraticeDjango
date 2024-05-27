from django.shortcuts import render
from .models import *

# Create your views here.
def main_page(request):
    return render(request, 'main.html')

def service_page(request):
    trainings = Training.objects.all()
    return render(request, 'service.html', {"trainings": trainings})

def about_page(request):
    return render(request, 'about.html')

def training_page(request, slug):
    training = Training.objects.get(slug=slug)
    return render(request, "training_page.html", {"training": training})

def list_page(request):
    regs = Registration.objects.all()
    return render(request, "list.html", {"regs": regs})