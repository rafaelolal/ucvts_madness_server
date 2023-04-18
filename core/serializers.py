"""All User serializers."""
from rest_framework import serializers
from .models import User, Bet


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


class BetCreateSerializer(serializers.ModelSerializer):
    """Used by Bet create view."""
    class Meta:
        model = Bet
        fields = ['user', 'game1', 'game2',
                  'game3', 'game4', 'game5',
                  'game6', 'game7', 'game8', 'game9', ]
