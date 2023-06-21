
from django.urls import path
from .views import meal_list,index,make_reservation
from . import views

urlpatterns = [
    path('make-reservation/', make_reservation, name='make_reservation'),
    path('', meal_list, name='meals'),
]

