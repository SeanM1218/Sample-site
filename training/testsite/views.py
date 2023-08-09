from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import patient, illness
from .forms import RegisterPatient

# Create your views here.
def index(response, id):
    ls = patient.objects.get(id=id)

    if response.method == "POST":
        if response.POST.get("save"):
            for illness in ls.illness_set.all():
                if response.POST.get("c" + str(illness.id)) == "clicked":
                    illness.treated = True
                else:
                    illness.treated = False
                illness.save()

        elif response.POST.get("newIllness"):
            txt = response.POST.get("new")

            if len(txt) > 2 and len(txt) < 300:
                ls.illness_set.create(text=txt, treated=False)

    return render(response, "testsite/profiles.html", {"ls":ls})

def home(response):
    ls = patient.objects.all()
    return render(response, "testsite/home.html", {})

def new_patient(response):
    if response.method == "POST":
        form = RegisterPatient(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            a = patient(name=n)
            a.save()
        
        return HttpResponseRedirect("/%i" %a.id)
    
    else:
        form = RegisterPatient()
    return render(response, "testsite/new_patient.html", {"form":form})