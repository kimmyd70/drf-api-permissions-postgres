from rest_framework import serializers
from .models import Woman

class WomanSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'added_by', 'name', 'description', 'category')
        model = Woman