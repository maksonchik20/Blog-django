from django.shortcuts import render
from .models import News
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def home(request):
    data = {
        "title": 'Блог',
        "news": News.objects.all()
    }
    return render(request, 'blog/home.html', data)

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
    # paginate_by = 3
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
    model = News
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True
        return False

class CreateNewsView(LoginRequiredMixin ,CreateView):
    model = News
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)


def contacti(request):
    return render(request, 'blog/contacti.html', {'title': 'Контакты'})
