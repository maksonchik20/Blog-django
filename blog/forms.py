from django.forms import ModelForm
from django.forms import Textarea
from .models import Contact, News
from captcha.fields import CaptchaField
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class UpdateForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        text = forms.CharField(widget=CKEditorUploadingWidget())
        model = News
        fields = ['title', 'text']

class ContentForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = News
        fields = [
            'title',
            'text'
        ]

class ContactForm(ModelForm):
    captcha = CaptchaField()
    def __init__(self, *args, **kwards):
        super(ContactForm, self).__init__(*args, **kwards)
        self.fields['first_name'].label = 'Имя'
        self.fields['last_name'].label = 'Фамилия'
        self.fields['message'].label = 'Сообщение'

    class Meta:
        # Определяем модель, на основе которой создаем форму
        model = Contact
        # Поля, которые будем использовать для заполнения
        fields = ['first_name', 'last_name', 'email', 'message', 'captcha']
        widgets = {
            'message': Textarea(
                attrs={
                    'placeholder': 'Напишите тут ваше сообщение'
                }
            ), 
            
        }