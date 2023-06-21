from django.db import models

# Create your models here.
class TableReservation(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    number_of_guests = models.IntegerField()
    date = models.DateField()
    time = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name



class Meal(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    details=models.CharField(max_length=333)
    time = models.CharField(max_length=20)
    def __str__(self):
        return self.name
class CHEFS(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Cake(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    details=models.CharField(max_length=333)
    def __str__(self):
        return self.name
