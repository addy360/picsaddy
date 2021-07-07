from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html")


def bio(request):
    return render(request, "bio.html")


def blog(request):
    return render(request, "blog.html")


def category(request, id):
    return render(request, "category.html")


def contact(request):
    return render(request, "contact.html")
