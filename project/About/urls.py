from django.urls import path
from About import views

urlpatterns = [
    path('', views.About, name='About'),
]