from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Blog(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.TextField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()
    image = models.FileField(upload_to="blogs")
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title


class Bio(models.Model):
    id = models.BigAutoField(primary_key=True)
    image = models.FileField(upload_to="biopics")
    title = models.TextField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title


class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    cat_name = models.CharField(max_length=20)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.cat_name

    def __repr__(self):
        return self.cat_name


class Gallery(models.Model):
    id = models.BigAutoField(primary_key=True)
    categories = models.ManyToManyField(Category)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to='gallery')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.author.username

    def __repr__(self):
        return self.author.username
