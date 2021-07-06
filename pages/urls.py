from pages.views import blog, category, contact, index, bio
from django.urls import path

urlpatterns = [
    path('', index, name="home"),
    path('blog', blog, name="blog"),
    path('category', category, name="category"),
    path('bio', bio, name="bio"),
    path('contact', contact, name="contact")
]
