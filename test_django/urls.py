from django.contrib import admin
from django.urls import path, include
from users import views as userViews
from django.contrib.auth import views as authViews
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from users.api import UserViewSet
from blog.api import NewsViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('news', NewsViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('blog.urls')),
    path('reg/', userViews.register, name='reg'),
    path('user/', authViews.LoginView.as_view(template_name='users/user.html'),name='auth'),
    path('pass-reset/', authViews.PasswordResetView.as_view(template_name='users/pass_reset.html'),name='pass-reset'),
    path('password_reset_confirm/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password_reset_complete/', authViews.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),
    path('password-reset/done/', authViews.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),    
    path('exit/', authViews.LogoutView.as_view(template_name='users/exit.html'),name='exit'),
    path('profile/', userViews.profile, name='profile'),
    # path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)