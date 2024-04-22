from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Moderator)
admin.site.register(PlayerRole)
admin.site.register(Tournament)
admin.site.register(Bracket)
admin.site.register(BracketColumn)
admin.site.register(Pairing)
admin.site.register(GameEntry)
admin.site.register(Schedule)