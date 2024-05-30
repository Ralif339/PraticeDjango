from django.shortcuts import render
from .models import *
from .forms import *
from transliterate import translit

# Create your views here.
def main_page(request):
    return render(request, 'main.html')

def service_page(request):
    trainings = Training.objects.all()
    return render(request, 'service.html', {"trainings": trainings})

def about_page(request):
    form = NewRecord()
    regs = Registration.objects.all()
    if (request.method == "POST"):
        form = NewRecord(request.POST)
        if (form.is_valid()):
            name = form.cleaned_data['name']
            title = form.cleaned_data['title']
            duration = form.cleaned_data['duration']
            date = form.cleaned_data['date']
            reg = Registration.objects.create(name=name, title=title, date=date, duration=duration)
            reg.save()
            return render(request, 'success.html')
    return render(request, 'about.html', {"form": form})

def training_page(request, slug):
    training = Training.objects.get(slug=slug)
    return render(request, "training_page.html", {"training": training})

def list_page(request):
    regs = Registration.objects.all()
    return render(request, "list.html", {"regs": regs})

def list_page_delete(request, id):
    try:
        reg = Registration.objects.get(id=id)
        reg.delete()
        regs = Registration.objects.all()
        return render(request, "list.html", {"regs": regs})
    except:
        regs = Registration.objects.all()
        return render(request, "list.html", {"regs": regs})