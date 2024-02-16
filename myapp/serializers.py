from rest_framework import serializers
from .models import Tour, TourCategory, Review, Booking, User
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ["url", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User(username=validated_data["username"])
        user.set_password(validated_data["password"])
        user.save()
        return user

class TourCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TourCategory
        fields = '__all__'

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'








