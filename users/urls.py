from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthViewSet, AccountViewSet, UserProfileRetrieve

router = DefaultRouter()
router.register(r'auth', AuthViewSet, basename='auth')
router.register(r'account', AccountViewSet, basename='account')

urlpatterns = [
    path('', include(router.urls)),
    path('<str:username>/', UserProfileRetrieve.as_view(), name='user-profile'),
]