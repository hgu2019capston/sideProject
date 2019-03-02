from django.urls import path
from . import views

app_name = 'peace'
urlpatterns = [
    path('', views.create, name='create'),
]
