from .models import TaggedItem
from rest_framework import serializers



class TaggeditemSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaggedItem
        fields = "__all__"