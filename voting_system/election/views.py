from http.client import HTTPResponse
from django.shortcuts import render
from .forms import Signup, Login
from .models import Account

def home (request):
    return render(request, 'home.html')

def signup (request):
    if request.method == 'POST':
        form = Signup(request.POST)
        if form.is_valid():
            passw = form.cleaned_data['passw']
            if passw == form.cleaned_data['cpassw']:
                name = form.cleaned_data['name']
                regno = form.cleaned_data['regno']
                user = Account(name = name, regno = regno, password = passw)
                user.save()
    else:
        form = Signup()
    return render(request, 'signup.html', {'form': form})

def login (request):
    if request.method == "POST":
        form = Login(request.POST)
        regno = form.cleaned_data["regno"]
        passw = form.cleaned_data["passw"]

        for object in Account.objects.all():
            if (regno == object.regno) and (passw == object.passw):
                    return HTTPResponse("Successful Login")
        
        return render (request, 'login.html', {"form":form, "error":"Bad Credentials"})

    else:
        form = Login()
        return render (request, 'login.html', {"form":form})
