from pages.views import blog, category, index, bio
from django.urls import path

urlpatterns = [
    path('', index, name="home"),
    path('blog', blog, name="blog"),
    path('category/<int:id>', category, name="category"),
    path('bio', bio, name="bio"),
]
