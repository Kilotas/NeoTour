from rest_framework.routers import DefaultRouter
from rest_framework import viewsets
from .views import TourListCreateAPIView, TourCategoryListCreateAPIView, ReviewListCreateAPIView, BookingListCreateAPIView
from django.urls import path
urlpatterns = [
    path('tours/', TourListCreateAPIView.as_view(), name='tour-list-create'),
    path('categories/', TourCategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('reviews/', ReviewListCreateAPIView.as_view(), name='review-list-create'),
    path('bookings/', BookingListCreateAPIView.as_view(), name='booking-list-create'),
]

