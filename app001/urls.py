from django.urls import path
from . import views

urlpatterns = [
    path('', views.first, name='first'),
    path('page1', views.hello, name='hello'),

]
