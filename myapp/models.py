from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TourCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'


class Tour(models.Model):
    category = models.ForeignKey(TourCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='tour_photos/')

    def __str__(self):
        return f"{self.name}"

class Review(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Booking(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number_of_people = models.IntegerField()
    phone_number = models.CharField(max_length=20)
    comments = models.TextField()


