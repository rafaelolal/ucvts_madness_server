from django.db.models import Model, OneToOneField, CASCADE
from django.db.models.fields import CharField, PositiveSmallIntegerField


class User(Model):
    id = CharField(max_length=28, primary_key=True)
    email = CharField(max_length=256)
    first_name = CharField(max_length=30, blank=True, null=True)
    middle_name = CharField(max_length=30, blank=True, null=True)
    last_name = CharField(max_length=30, blank=True, null=True)
    points = PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"{self.email}, {self.points} points"


class Bet(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    order = CharField(max_length=4096)

    def __str__(self):
        return f"{self.user.email}"


class GameCount(Model):
    count = PositiveSmallIntegerField()

    def __str__(self):
        return f"Count: {self.count}"
