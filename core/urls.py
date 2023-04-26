from django.urls import path
from .views import UserCreateView, UserListView, BetCreateView, BetRetrieveView, leaderboard_update_view

urlpatterns = [
    path('user/create/', UserCreateView.as_view(), name='user-create'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('bet/create/', BetCreateView.as_view(), name='bet-create'),
    path('user/<str:user>/bet/', BetRetrieveView.as_view(), name='bet-retrieve'),
    path('leaderboard/update/', leaderboard_update_view,
         name='leaderboard-update'),
]
