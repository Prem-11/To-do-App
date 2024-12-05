from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('agent_id','TodoTitle','TodoDesc','Category','DueDate')