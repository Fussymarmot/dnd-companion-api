from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RacesViewSet, SpellsViewSet, MonstersViewSet, CharactersClassViewSet

router = DefaultRouter()

router.register(r'races', RacesViewSet)
router.register(r'spells', SpellsViewSet)
router.register(r'monsters', MonstersViewSet)
router.register(r'characters_class', CharactersClassViewSet)


urlpatterns = [
    path('', include(router.urls)),
]