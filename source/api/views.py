from django.shortcuts import render
from rest_framework import viewsets

from api.models import Quote, Rating
from api.serializers import QuoteSerializer

class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer