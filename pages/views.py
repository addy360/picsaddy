from pages.models import Bio, Blog, Category, Gallery
from django.shortcuts import render
from pprint import pprint

# Create your views here.


def index(request):
    categories = Category.objects.all()
    formated = []
    for cat in categories:
        res = cat.images(f'{cat.id}')
        formated.append({"name": cat.cat_name,
                        "photo_count": res[0], "url": res[1], })
    context = {"categories": formated}
    return render(request, "index.html", context=context)


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
