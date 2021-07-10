from django.db import models

# Create your models here.


class Contact(models.Model):
    id = models.BigAutoField(primary_key=True)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.email} - {self.subject}'
