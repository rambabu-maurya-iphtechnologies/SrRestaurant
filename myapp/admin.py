from django.contrib import admin
from .models import TableReservation,Meal,CHEFS,Cake

class TableReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'number_of_guests', 'date', 'time', 'message')

admin.site.register(TableReservation, TableReservationAdmin)

class MealAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'time','image')

admin.site.register(Meal, MealAdmin)
class CHEFSAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(CHEFS, CHEFSAdmin)

class CakeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price','image')

admin.site.register(Cake, CakeAdmin)