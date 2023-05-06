from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'product', ProductViewSet, basename="product")

new_pattern = router.urls