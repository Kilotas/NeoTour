from django.contrib import admin
from .models import Tour, TourCategory, Review, Booking
# Register your models here.
admin.site.register(Tour)
admin.site.register(TourCategory)
admin.site.register(Review)
admin.site.register(Booking)