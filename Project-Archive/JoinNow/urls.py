from django.urls import path
from JoinNow import views

urlpatterns = [
    path('', views.JoinNow, name='JoinNow'),
]