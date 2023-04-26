"""All serializers."""
from rest_framework import serializers
from .models import User, Bet, GameCount


class UserCreateSerializer(serializers.ModelSerializer):
    """Used by User create view."""
    class Meta:
        model = User
        fields = ['id', 'email']


class UserListSerializer(serializers.ModelSerializer):
    """Used by User list view."""

    name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['name', 'points']

    def get_name(self, obj):
        if all([obj.first_name, obj.middle_name, obj.last_name]):
            return f"{obj.first_name} {obj.middle_name} {obj.last_name}"

        return obj.email


class BetSerializer(serializers.ModelSerializer):
    """Used by Bet create and retrieve view."""
    class Meta:
        model = Bet
        fields = ['user', 'order']


class GameCountSerializer(serializers.ModelSerializer):
    """Used by GameCount create and retrieve view."""
    class Meta:
        model = GameCount
        fields = ['count']
