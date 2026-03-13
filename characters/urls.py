from django.urls import path, include
from .views import CharacterViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'characters', CharacterViewSet)
urlpatterns = [
   path('', include(router.urls)),
]