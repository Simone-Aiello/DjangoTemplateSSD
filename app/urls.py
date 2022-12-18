from rest_framework.routers import SimpleRouter

from app.views import SuperHeroViewSet

router = SimpleRouter()
router.register('', SuperHeroViewSet, basename='superhero')

urlpatterns = router.urls
