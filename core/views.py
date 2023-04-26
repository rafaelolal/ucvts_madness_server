"""All User API views."""
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from .serializers import UserCreateSerializer, UserListSerializer, BetSerializer, GameCountSerializer
from .models import User, Bet, GameCount
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED


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
    serializer_class = BetSerializer


class BetRetrieveView(RetrieveAPIView):
    """Retrieves a Bet."""
    queryset = Bet.objects.all()
    serializer_class = BetSerializer
    lookup_field = 'user'


@api_view(['POST'])
def leaderboard_update_view(request):
    """Updates the game count if it is different and refreshes leaderboard"""

    results = [None]*7
    game_count = GameCount.objects.get(pk=1)

    for i, game in enumerate(request.data):
        winner = None
        if game['isFinished']:
            winner = game['team1Name'] if game['team1Points'] > game['team2Points'] else game['team2Name']
        results[i] = winner

    if 7-results.count(None) != game_count.count:
        game_count.count = 7-results.count(None)
        game_count.save()

        print("New rankings")
        for bet in Bet.objects.all():
            entries = bet.order.split("*")
            points = 0
            for entry, result in zip(entries, results):
                if result and entry in result:
                    points += 1

            bet.user.points = points
            bet.user.save()

    return Response(status=HTTP_201_CREATED)
