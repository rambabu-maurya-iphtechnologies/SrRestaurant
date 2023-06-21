from django.shortcuts import render,redirect
from .models import *
from django.shortcuts import render
from .models import TableReservation
def index(request):
    return render(request,"index.html")

from datetime import datetime

def make_reservation(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        number_of_guests = request.POST.get('number-guests')
        date_str = request.POST.get('date')
        time = request.POST.get('time')
        message = request.POST.get('message')

        # Convert the date string to a datetime object
        date = datetime.strptime(date_str, '%d.%m.%Y').strftime('%Y-%m-%d')

        # Save the reservation data to the database
        reservation = TableReservation(
            name=name,
            email=email,
            phone=phone,
            number_of_guests=number_of_guests,
            date=date,
            time=time,
            message=message
        )
        reservation.save()

        return render(request, 'success.html')  # Replace 'success.html' with your success template
    else:
        return render(request, 'index.html')  # Replace 'index.html' with the name of your template file

from django.shortcuts import render
from django.http import HttpResponse
from .models import Meal,Cake

def meal_list(request):
    print("enter in meal........")
    meals = Meal.objects.all()
    
    mealsBreakfast = Meal.objects.filter(time="Breakfast")
    mealsDinner = Meal.objects.filter(time="Dinner")
    mealsLunch=Meal.objects.filter(time="Lunch")
    chefs = CHEFS.objects.all()
    CakeS = Cake.objects.all()
    print(meals)
    context = {'meals': meals,
    'mealsd': mealsDinner,
    'mealsb': mealsBreakfast,
    'mealsl':mealsLunch,
    'chefs': chefs,
    'cake':CakeS}
    print(context)
    return render(request, 'index.html', context)