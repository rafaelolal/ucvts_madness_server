from django.urls import path
from .views import UserCreateView, UserListView, BetCreateView

urlpatterns = [
    path('user/create/', UserCreateView.as_view(), name='user-create'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('bet/create/', BetCreateView.as_view(), name='bet-create'),
]
