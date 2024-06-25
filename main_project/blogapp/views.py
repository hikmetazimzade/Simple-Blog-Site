from django.shortcuts import render, redirect
from .models import BlogModel, CommentModel
from .forms import BlogForm, CommentForm
from django.contrib import messages
from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup



def blogs(request):
    # Putting it to Celery Would be much more efficient
    request_data = requests.get("https://weather.tomorrow.io/")
    soup = BeautifulSoup(request_data.text, "html.parser")

    temperature = soup.find(attrs = {"class" : "_3fQrr5"}).getText()
    curr_blogs = BlogModel.objects.all()
    
    return render(request, "blogapp/blogs.html", {
        "curr_blogs" : curr_blogs,
        "temperature" : temperature
    })


def blog(request, id):
    try:
        curr_blog = BlogModel.objects.get(id = id)
        comments = curr_blog.commentmodel_set.all()
        
    except:
        return redirect("home")

    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.error(request, "You should login to write a comment!")
            return redirect("home")
        
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data.get("comment", "")
            CommentModel.objects.create(content = comment, star_number = 5, blog = curr_blog, user = request.user)

    else:
        form = CommentForm()
    
    return render(request, "blogapp/blog.html", {
        "curr_blog" : curr_blog,
        "comments" : comments,
        "form" : form
    })


def create_blog(request):
    if request.method == "GET":
        form = BlogForm()
        return render(request, "blogapp/create_blog.html", {
            "form" : form
        })
    
    else:
        form = BlogForm(request.POST, request.FILES)

        if form.is_valid():
            content_data = form.cleaned_data.get("content", "")
            blog_name = form.cleaned_data.get("blog_name")
            
            BlogModel.objects.create(blog_name = blog_name, like_number = 0, content = content_data, user = request.user)
            return redirect("blogs")
        
        return render(request, "blogapp/create_blog.html", {
            "form" : form
        })
    

def like_blog(request, id):
    if request.method == "POST":
        try:
            curr_blog = BlogModel.objects.get(id = id)
            curr_blog.like_number += 1
            curr_blog.save()
            return JsonResponse({'success': True, 'like_number': curr_blog.like_number}
        )
        except:
            return JsonResponse({"success" : False})
        
    return JsonResponse({"success" : False})