from django.urls import path,include
from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
]