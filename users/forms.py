from dataclasses import fields
import email
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserOurRegistation(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    # def clean_email(self):
    #     email = self.cleaned_data['email'].strip()
    #     if User.objects.filter(email_iexact=username).exists():
    #         raise forms.ValidationError('')
    #     return email

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileImage(forms.ModelForm):
    def __init__(self, *args, **kwards):
        super(ProfileImage, self).__init__(*args, **kwards)
        self.fields['img'].label = 'Изображение профиля'

    class Meta:
        model = Profile
        fields = ['img']