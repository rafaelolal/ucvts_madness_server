from django.contrib import admin

from .models import User, Bet, GameCount

# Register your models here.
admin.site.register(User)
admin.site.register(Bet)
admin.site.register(GameCount)
