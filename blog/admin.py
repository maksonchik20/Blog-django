from django.contrib import admin
from .models import News, Contact
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class NewsAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'

class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm


# admin.site.register(News)
admin.site.register(Contact)

admin.site.register(News, NewsAdmin)