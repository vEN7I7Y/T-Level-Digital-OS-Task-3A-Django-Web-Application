from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.urls import reverse_lazy
from django.views.generic import CreateView
from main.forms import *
from django.http import HttpResponseRedirect
import cryptography
from cryptography import fernet 


#creating the homepage view
def index(request):
    return render (request, "index.html")
#creating the other views

def articles(request):
    return render(request, "articles.html")

#view for the energy usage calculation
def energyUsage(request):
    if request.method == "POST":
            form = energy_usageForm(request.POST)
            if form.is_valid():
                form.save()
    else:
            form = energy_usageForm()
    return render(request,"energyusage.html",{"form" : form})

#signup and user based views

class signupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def profile(request):
    #imports the data from the database
    data = appointmentModel.objects.all()
    return render(request, "registration/profile.html", {"data" : data})

#view for the payment form 
def payment(request):
    url = reverse_lazy("profile")
    #form collecting data and handling it
    if request.method == "POST":
        form = paymentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(url)
    else:
        form = paymentForm()
    return render(request, "registration/payment.html", {"form" : form})

#view for the appointment form
def appointment(request):
    url = reverse_lazy("payment")
    if request.method == "POST":
        form = appointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(url)
    else:
        form = appointmentForm()
    return render(request, "registration/bookappointment.html", {"form" : form})

#view for the carbon footprint calculation
def carbonFootprint(request):
    if request.method == "POST":
        form = carbonForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = carbonForm()
    return render(request, "registration/carbonprintcalc.html", {"form" : form})
