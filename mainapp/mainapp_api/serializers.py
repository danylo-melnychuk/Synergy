from rest_framework import serializers
from ..models import UserOfGroup, GroupOfUser

class UserSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = UserOfGroup
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = GroupOfUser
        fields = '__all__'