from django.contrib import admin
from teams.models import *
# Register your models here.

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['playerName','team','role',]

class PlayerInline(admin.TabularInline):  
    model = Player
    extra = 1

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['teamName','image','description','price',]
    inlines = [PlayerInline]

@admin.register(TeamList)
class TeamListAdmin(admin.ModelAdmin):
    list_display = ['playerTeam',]