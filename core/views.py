"""All User API views."""
from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import UserCreateSerializer, UserListSerializer, BetCreateSerializer
from .models import User, Bet


class UserCreateView(CreateAPIView):
    """Creates a User."""
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserListView(ListAPIView):
    """Lists Users."""
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class BetCreateView(CreateAPIView):
    """Creates a Bet."""
    queryset = Bet.objects.all()
    serializer_class = BetCreateSerializer
