from django.urls import path
from .import views


urlpatterns = [
    path(route = "", view = views.blogs, name = "blogs"),
    path(route = "<int:id>", view = views.blog, name = "blog"),
    path(route = "create_blog", view = views.create_blog, name = "create_blog"),
    path(route = "like_blog/<int:id>", view = views.like_blog, name = "like_blog"),
]