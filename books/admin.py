from django.contrib import admin
from .models import *
from borrowdetails.models import *
# Register your models here.

admin.site.register(BookModel)
admin.site.register(CustomUser)
admin.site.register(BorrowModel)