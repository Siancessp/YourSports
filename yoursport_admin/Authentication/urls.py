from django.urls import path
from .views import (RegistrationAPIView, LoginAPIView, PricingListAPIView,
                    ContactListCreateAPIView,ContactRetrieveUpdateDestroyAPIView,
                    UserListCreateAPIView ,UserRetrieveUpdateDestroyAPIView
                    ,ForgotPasswordAPIView ,ResetPasswordAPIView, StaffUserListAPIView,
                    FootballTeamCreateAPIView, PlayerDetailAPIView)

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('pricings/', PricingListAPIView.as_view(), name='pricing-list'),
    path('contacts/', ContactListCreateAPIView.as_view(), name='contact-list-create'),
    path('contacts/<int:pk>/', ContactRetrieveUpdateDestroyAPIView.as_view(), name='contact-retrieve-update-destroy'),
    path('users/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user-retrieve-update-destroy'),
    path('forgot-password/', ForgotPasswordAPIView.as_view(), name='forgot-password'),
    path('reset-password/', ResetPasswordAPIView.as_view(), name='reset-password'),
    path('create-team/', FootballTeamCreateAPIView.as_view(), name='create-team'),
    path('staff-users/', StaffUserListAPIView.as_view(), name='staff-users-list'),
    path('staff-users/<int:pk>/', StaffUserListAPIView.as_view(), name='staff-user-detail'),
    path('player-details/', PlayerDetailAPIView.as_view(), name='player-details-list'),
    path('player-details/<int:pk>/', PlayerDetailAPIView.as_view(), name='player-detail'),
]
