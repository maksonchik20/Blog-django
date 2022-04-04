from email.policy import default
from tkinter import CASCADE
from turtle import title
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    avtor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})