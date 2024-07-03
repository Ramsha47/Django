from django.urls import path, include
from myapp.views.homeview import home

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
   
]