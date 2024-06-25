from django.shortcuts import render
from .models import ContactModel, AboutModel
import requests
from bs4 import BeautifulSoup


def home(request):
    # Putting it to Celery Would be much more efficient
    request_data = requests.get("https://weather.tomorrow.io/")
    soup = BeautifulSoup(request_data.text, "html.parser")

    temperature = soup.find(attrs = {"class" : "_3fQrr5"}).getText()
    return render(request, "mainapp/home.html", {
        "temperature" : temperature
    })


def contact(request):
    try:
        content = ContactModel.objects.get(pk = 1).content
    except:
        content = "About Us"

    return render(request, "mainapp/contact.html", {
        "content" : content
    })


def about(request):
    try:
        content = AboutModel.objects.get(pk = 1).content
    except:
        content = "About Us"


    return render(request, "mainapp/about.html", {
        "content" : content
    })