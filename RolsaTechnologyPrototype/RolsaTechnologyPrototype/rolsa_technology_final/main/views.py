from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.urls import reverse_lazy
from django.views.generic import CreateView
from main.forms import *
from django.http import HttpResponseRedirect, Http404
import cryptography
from cryptography import fernet


# creating the homepage view
def index(request):
    try:
        return render(request, "index.html")
    except:
        raise Http404()


# creating the other views


# articles and its sub views
def articles(request):
    try:
        return render(request, "articles.html")
    except:
        raise Http404()


def privacy_policy(request):
    try:
        return render(request, "privacypolicy.html")
    except:
        raise Http404()


def cookies_policy(request):
    try:
        return render(request, "cookiespolicy.html")
    except:
        raise Http404()


# view for the energy usage calculation
def energyUsage(request):
    try:
        # initialises the form
        if request.method == "POST":
            form = energy_usageForm(request.POST)
            if form.is_valid():
                form.save()
    except:
        # template returns an error if there is an issue
        raise Http404()

    else:
        # renders a blank instance of the form if the template request isnt post
        form = energy_usageForm()
    # renders the template
    return render(request, "energyusage.html", {"form": form})


# signup and user based views


class signupView(CreateView):
    try:
        # initialises the built in sign up form
        form_class = UserCreationForm
        # the url to redirect to if it is successful
        success_url = reverse_lazy("login")
        # limks the template with the view
        template_name = "registration/signup.html"
    except:
        raise Http404()


def profile(request):
    try:
        # imports the data from the database
        data = appointmentModel.objects.all()
        # renders the data in the template in the context data
        return render(request, "registration/profile.html", {"data": data})
    except:
        raise Http404()


# view for the payment form
def payment(request):
    # the redirect url
    url = reverse_lazy("profile")
    # form collecting data and handling it
    try:
        if request.method == "POST":
            form = paymentForm(request.POST)
            if form.is_valid():
                form.save()
                # redirects user to the url mentioned above
                return HttpResponseRedirect(url)
    except:
        # template returns an error if there is an issue
        raise Http404()
    else:
        # creates a blank instance of the form, if the template request isnt post
        form = paymentForm()
    # renders the template with the form
    return render(request, "registration/payment.html", {"form": form})


# view for the appointment form
def appointment(request):
    # the redirect url
    url = reverse_lazy("payment")
    # form collecting data and handling it
    try:
        if request.method == "POST":
            form = appointmentForm(request.POST)
            if form.is_valid():
                form.save()
                # redirects user to the url mentioned above
                return HttpResponseRedirect(url)
    except:
        # template returns an error if there is an issue
        raise Http404()
    else:
        # creates a blank instance of the form if the template request isnt post
        form = appointmentForm()
    # renders the template with the form
    return render(request, "registration/bookappointment.html", {"form": form})


# view for the carbon footprint calculation
def carbonFootprint(request):
    try:
        # form collecting data and handling it
        if request.method == "POST":
            form = carbonForm(request.POST)
            if form.is_valid():
                form.save()
    except:
        # template returns an error if there is an issue
        raise Http404()
    else:
        # creates a blank instance of the form if the template request isnt post
        form = carbonForm()
    # renders the template with the form
    return render(request, "registration/carbonprintcalc.html", {"form": form})
