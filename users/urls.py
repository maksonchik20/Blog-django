from rest_framework import routers
from users.api import UserViewSet


router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = router.urls