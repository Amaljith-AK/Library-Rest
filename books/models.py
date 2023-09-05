from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class BookModel(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='book_template')
    author=models.CharField(max_length=100)
    isbn=models.IntegerField()
    genre=models.CharField(max_length=150)
    available=models.BooleanField(default=True)
    borrowed_count=models.IntegerField(default=0)

    def __str__(self):
        return self.title
    

class CustomUser(AbstractUser):
    BorrowCount=models.IntegerField(default=0)