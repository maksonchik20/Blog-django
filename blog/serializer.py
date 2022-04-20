from .models import News
from rest_framework import serializers

class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=News
        fields = ['id', 'title', 'text', 'date', 'avtor']