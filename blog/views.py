from django.shortcuts import render, redirect
from .models import News, Contact, User
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.core.mail import send_mail
from .forms import ContactForm, ContentForm, UpdateForm
from django.db.models import Q
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class ContactCreate(CreateView):
    model = Contact
    # fields = ["first_name", "last_name", "message"]
    success_url = reverse_lazy('success_page')
    form_class = ContactForm

    def form_valid(self, form):
        # Формируем сообщение для отправки
        data = form.data
        subject = f'Сообщение с формы от {data["first_name"]} {data["last_name"]} Почта отправителя: {data["email"]}'
        email(subject, data['message'])
        return super().form_valid(form)

def email(subject, content):
   send_mail(subject,
      content,
      'отправитель@gmail.com',
      ['maksonchik505@gmail.com']
   )

# Функция, которая вернет сообщение в случае успешного заполнения формы
def success(request):
    messages.success(request, f'Ваше сообщение успешно отправлено')
    return redirect('blog-contacti') 

def home(request):
    data = {
        "title": 'Блог',
        "news": News.objects.all()
    }
    return render(request, 'blog/home.html', data)

def resume(request):
    data = {
        "title": 'Обо мне',
    }
    return render(request, 'blog/resume.html', data)

class DeleteNewsView(LoginRequiredMixin,UserPassesTestMixin ,DeleteView):
    model = News
    success_url = "/"
    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True
        return False

class ShowNewsView(ListView):
    model = News
    template_name = 'blog/home.html'
    context_object_name = 'news'
    ordering = ['-date']
    paginate_by = 5
    
    def get_queryset(self): # новый
        query = self.request.GET.get('q')
        if query is None:
            query = ''
        object_list = News.objects.filter( Q(title__contains=query) | Q(text__contains=query)).order_by('-date')
        return object_list

    def get_context_data(self, **kwards):
        ctx = super(ShowNewsView, self).get_context_data(**kwards)
        ctx['title'] = 'Главная страница блога'
        return ctx

class NewsDetailView(DetailView):
    model = News

    def get_context_data(self, **kwards):
        ctx = super(NewsDetailView, self).get_context_data(**kwards)
        ctx['title'] = News.objects.filter(pk=self.kwargs['pk']).first()
        return ctx

class UpdateNewsView(LoginRequiredMixin,UserPassesTestMixin ,UpdateView):
    # model = News
    # text = forms.CharField(widget=CKEditorUploadingWidget())
    # fields = ['title', 'text']
    form_class = UpdateForm
    template_name='blog/news_update.html'
    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)
    def get_queryset(self):
        model=News
        return News.objects

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True
        return False

class CreateNewsView(LoginRequiredMixin ,CreateView):
    # model = News
    # content = forms.CharField(widget=CKEditorWidget, label='')
    # fields = ['title', 'text']
    form_class = ContentForm
    template_name = 'blog/news_form.html'

    def get_queryset(self):
        model=News
        return News.objects
        
    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)

class UserPosts(ListView):
    model = User
    template_name = 'blog/user_posts.html'
    context_object_name = 'users'
    # ordering = ['-date']
    paginate_by = 5
    
    # def get_queryset(self): # новый
    #     query = self.request.GET.get('q')
    #     if query is None:
    #         query = ''
    #     object_list = News.objects.filter( Q(title__contains=query) | Q(text__contains=query))
    #     return object_list

    def get_context_data(self, **kwards):
        model = User
        ctx = super(UserPosts, self).get_context_data(**kwards)
        ctx['title'] = 'Поиск статьи пользователя'
        ctx['all_user'] = User.objects.all().count()
        # ctx['all_admin'] = User.objects.filter('ADMIN'==True).count
        return ctx

def contacti(request):
    return render(request, 'blog/contacti.html', {'title': 'Контакты'})
