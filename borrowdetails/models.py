from typing import Iterable, Optional
from django.db import models
from books.models import BookModel
from datetime import datetime
from books.models import CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class BorrowModel(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    book=models.ForeignKey(BookModel,on_delete=models.CASCADE)
    date_of_borrow=models.DateField(auto_now_add=True)
    date_of_return=models.DateField()
    fine=models.IntegerField(default=0)
    returned=models.BooleanField(default=False)


    def __str__(self):
        return self.user,self.book