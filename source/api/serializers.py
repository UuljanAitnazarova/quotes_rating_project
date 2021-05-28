from rest_framework import serializers
from api.models import Quote, Rating


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ['id', 'text', 'author', 'email', 'is_moderated', 'created_at']
        read_only_fields = ['is_moderated', 'created_at']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'user', 'quote', 'rating']


