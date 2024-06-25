from django.urls import path
from .import views


urlpatterns = [
    path(route = "", view = views.home, name = "home"),
    path(route = "home", view = views.home, name = "home"),
    path(route = "about", view = views.about, name = "about"),
    path(route = "contact", view = views.contact, name = "contact"),
]