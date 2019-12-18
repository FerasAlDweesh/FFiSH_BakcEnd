from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import (
UserCreateAPIView,
CardList,
VendorList,
PointList,
RewardList,
ProfileDetails,
)


urlpatterns = [
    path('login/', TokenObtainPairView.as_view() , name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
  
    path('cards/', CardList.as_view(), name='card-list'),
    path('vendors/', VendorList.as_view(), name='vendor-list'),
    path('points/', PointList.as_view(), name='points'),
    path('Rewards/', RewardList.as_view(), name='rewards'),

    path('profile/', ProfileDetails.as_view(), name="profile"),
]