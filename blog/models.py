from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from captcha.fields import CaptchaField
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class News(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    avtor = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    message = models.TextField(max_length=2000)
    captcha = CaptchaField()


    def __str__(self):
        return self.email

