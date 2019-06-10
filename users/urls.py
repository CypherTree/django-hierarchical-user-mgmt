from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, RoleViewSet, UserViewSet

router = DefaultRouter()

router.register('user', UserViewSet, basename='user')
router.register('category', CategoryViewSet, basename='category')
router.register('role', RoleViewSet, basename='role')

urlpatterns = router.urls
