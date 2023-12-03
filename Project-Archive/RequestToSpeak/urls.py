from django.urls import path
from RequestToSpeak import views

urlpatterns = [
    path('', views.RequestToSpeak, name='RequestToSpeak'),
]