from . import views
from django.urls import path, include
from rest_framework import routers
from blog.api import NewsViewSet


router = routers.DefaultRouter()
router.register('news', NewsViewSet)

urlpatterns = [
    path('', views.ShowNewsView.as_view(), name='blog-home'),
    path('posts/', views.UserPosts.as_view(), name='user-posts'),
    path('resume/', views.resume, name='resume'),
    path('contacti/', views.ContactCreate.as_view(template_name='blog/contacti.html'), name='blog-contacti'),
    path('success/', views.success, name='success_page'),
    path('news/<int:pk>/', views.NewsDetailView.as_view(), name='news-detail'),
    path('news/add/', views.CreateNewsView.as_view(), name='news-add'),
    path('news/<int:pk>/update/', views.UpdateNewsView.as_view(), name='news-update'),
    path('news/<int:pk>/delete/', views.DeleteNewsView.as_view(), name='news-delete'),
    path('', include(router.urls))
]