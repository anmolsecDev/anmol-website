from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request, "homepage.html")


def about(request):
    return render(request, "about.html")


def donate(request):
    return render(request, "donate.html")


def contact(request):
    return render(request, "contact.html")
