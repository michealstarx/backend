from django.shortcuts import render

from .models import Smartify
from .serializers import SmartifySerializer

from rest_framework import mixins, generics, viewsets

class List(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = SmartifySerializer
    queryset = Smartify.objects.all()

class Data(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = SmartifySerializer
    queryset = Smartify.objects.all()

    lookup_field = 'id'