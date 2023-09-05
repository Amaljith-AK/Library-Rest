from django.urls import path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from .views import BorrowMVS
route=DefaultRouter()

route.register('borrow',BorrowMVS,basename='borrow')

urlpatterns=[

]+route.urls