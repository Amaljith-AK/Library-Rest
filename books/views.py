from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import BookSer,UserSer
from .models import BookModel,CustomUser
from rest_framework import authentication,permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from borrowdetails.serializers import BorrowSer
# Create your views here.



class BookMVS(ModelViewSet):
    serializer_class=BookSer
    queryset=BookModel.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        ser=BookSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'msg':'Book detail successfully added'})
        return Response(data=ser.errors)
    


    @action(methods=['POST'],detail=True)
    def borrow_this_book(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        book=BookModel.objects.get(id=id)
        user=request.user
        ser=BorrowSer(data=request.data)
        if ser.is_valid():
            book.available=False
            book.borrowed_count += 1
            book.save()
            user.BorrowCount += 1
            user.save()
            ser.save(user=user,book=book)
            return Response(data=ser.data)
        return Response(data=ser.errors)


    

class signupMVS(ModelViewSet):
    def create(self, request, *args, **kwargs):
        ser=UserSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'msg':'signup successful'})
        return Response(data=request.data)
    
class UserDetails(ModelViewSet):
    queryset=CustomUser.objects.all()
    serializer_class=UserSer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
