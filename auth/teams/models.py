from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import uuid


class Team(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # user = models.ForeignKey(UserAccount,on_delete=models.SET_NULL,null=True)
    teamName = models.CharField(max_length=100)
    image = models.ImageField(null=True,blank=True,default = "/images/placeholder.png",upload_to="images/")
    description = models.TextField(null=True,blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    createdAt = models.DateTimeField(auto_now_add=True)
    class Meta:
        permissions = [
            ("view_teams", "Can view team details"),
            # Add more custom permissions as needed
        ]

    def __str__(self):
        return self.teamName
    
class TeamList(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    playerTeam = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.playerTeam
    

class Player(models.Model):
    PLAYER_ROLES = [
        ('WK', 'Wicket Keeper'),
        ('BWL', 'Bowler'),
        ('BAT', 'Batsman'),
    ]
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    playerName = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    role = models.CharField(max_length=3, choices=PLAYER_ROLES,null=True)

    def __str__(self):
        return self.playerName