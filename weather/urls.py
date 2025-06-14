from rest_framework.routers import DefaultRouter
from .views import weatherView

# user_city = str
router = DefaultRouter()
router.register('api/weather', weatherView, 'weather')

urlpatterns = router.urls

