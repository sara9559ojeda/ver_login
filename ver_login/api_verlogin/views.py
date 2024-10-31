import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import login 
from .serializer import login_serializer # serializer clases encargadas de 

# Create your views here.

class loginApiView(APIView):


    def get(self, request, *args, **kwargs):
        lista_login=login.objects.all()# objects.all = select * table
        serializer_login=login_serializer(lista_login, many=True) #
        print(serializer_login)
        return Response(serializer_login.data, status=status.HTTP_200_OK)
    def post(self, request, *args, **kwargs): #post: create
        data={
            'user':request.data.get('user'),
            'password':request.data.get('password'),
        }
        serializador=login_serializer(data=data)
        if serializador.is_valid():
            serializador.save()
            return Response (serializador.data, status=status.HTTP_201_CREATED)
        return Response (serializador.data, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, pkid): #actualizar/ el pkid puede ser cualquier otra variable ej: x
        micuenta= login.objects.filter(id=pkid).update(
            user=request.data.get('user'),
            password=request.data.get('password'),
        )
        return Response(micuenta, status=status.HTTP_200_OK)   
    def delete(self, request, pkid): #eliminar/ el pkid puede ser cualquier otra variable ej: x
        cuentaeliminada= login.objects.filter(id=pkid).delete()
        return Response(cuentaeliminada, status=status.HTTP_204_NO_CONTENT)
class validateApiView(APIView):
    def post(self, request, *args, **kwargs):
        data={
            'user':request.data.get('user'),
            'password':request.data.get('password'),
        }
        if login.objects.filter(user=data['user'], password=data['password']).exists():
            return Response(True, status=status.HTTP_200_OK) #ver perfil
        return Response(False, status=status.HTTP_400_BAD_REQUEST)