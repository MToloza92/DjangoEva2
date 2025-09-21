from rest_framework.routers import DefaultRouter
from .views import BodegaViewSet

router = DefaultRouter()
router.register(r'bodegas', BodegaViewSet)

urlpatterns = router.urls
