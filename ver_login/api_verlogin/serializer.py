from .models import login
from rest_framework import serializers 

class login_serializer(serializers.ModelSerializer):
    class Meta:
        model=login
        fields=[ #muestra lo que va a aparecer en postman
            'id',
            'user', 'password']