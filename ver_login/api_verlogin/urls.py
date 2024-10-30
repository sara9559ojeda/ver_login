from django.urls import path
from .views import loginApiView
from .views import validateApiView
from .validate import validate_jwt


urlpatterns=[
    path('list', loginApiView.as_view()), 
    path('crear-userpassword', loginApiView.as_view()), 
    path('actualizar-userpassword/<int:pkid>', loginApiView.as_view(), name='actualizar-userpassword'),
    path('borrar-userpassword/<int:pkid>', loginApiView.as_view(), name='borrar-userpassword'),
    path('login', validateApiView.as_view()),
   
   
]