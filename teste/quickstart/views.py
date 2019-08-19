from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from quickstart.models import Phrase
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer, PhraseSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class PhraseViewSet( viewsets.ModelViewSet):
    queryset = Phrase.objects.all()
    serializer_class = PhraseSerializer
