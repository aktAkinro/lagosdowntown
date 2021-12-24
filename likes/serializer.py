from .models import LikedItem
from rest_framework import serializers



class LikeditemSerializer(serializers.ModelSerializer):

    class Meta:
        model = LikedItem
        fields = ['object_id']