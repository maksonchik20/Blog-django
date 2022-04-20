from rest_framework import viewsets
from .models import News
from blog.serializer import NewsSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset=News.objects.all()
    serializer_class=NewsSerializer