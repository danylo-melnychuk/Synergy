from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import UserSerializer, GroupSerializer
from  ..models import UserOfGroup, GroupOfUser


class UserView(viewsets.ModelViewSet):

    queryset = UserOfGroup.objects.all()
    serializer_class = UserSerializer


class GroupView(viewsets.ModelViewSet):
    queryset = GroupOfUser.objects.all()
    serializer_class = GroupSerializer
