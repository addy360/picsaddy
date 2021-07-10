from pprint import pp, pprint

from django.shortcuts import render

from pages.helper import format_categories, validate_post_data
from pages.models import Bio, Blog, Category, Gallery

# Create your views here.


def index(request):
    categories = Category.objects.all()
    formated = format_categories(categories)
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
    images = Gallery.objects.filter(
        categories=id).prefetch_related('categories')
    # TODO fix this!!!
    cat = Category.objects.get(id=id).cat_name
    context = {"images": images, "category_name": cat,
               "total_images": images.count()}
    return render(request, "category.html", context=context)


def contact(request):
    if request.method == "POST":
        errors, clean_data = validate_post_data(request)
        if len(errors):
            context = {"errors": errors}
            return render(request, "contact.html", context)
        print('[+] all data are clean')

    return render(request, "contact.html")
