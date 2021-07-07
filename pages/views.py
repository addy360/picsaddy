from pages.models import Blog
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html")


def bio(request):
    return render(request, "bio.html")


def blog(request):
    blogs = Blog.objects.all()
    context = {"blogs": blogs}
    print(context)
    return render(request, "blog.html", context=context)


def category(request, id):
    return render(request, "category.html")


def contact(request):
    return render(request, "contact.html")
