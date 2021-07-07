from pages.models import Bio, Blog
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html")


def bio(request):
    bios = Bio.objects.all()
    context = {"bios": bios}
    return render(request, "bio.html", context=context)


def blog(request):
    blogs = Blog.objects.all()
    context = {"blogs": blogs}
    return render(request, "blog.html", context=context)


def category(request, id):
    return render(request, "category.html")


def contact(request):
    return render(request, "contact.html")
