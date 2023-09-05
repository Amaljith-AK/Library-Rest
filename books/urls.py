from django.urls import path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from books.views import signupMVS,BookMVS,UserDetails
route=DefaultRouter()

route.register('user',signupMVS,basename='signup')
route.register('books',BookMVS,basename='allbooks')
route.register('userdet',UserDetails,basename='userdet')


urlpatterns=[
    path('token/',views.obtain_auth_token),
]+route.urls