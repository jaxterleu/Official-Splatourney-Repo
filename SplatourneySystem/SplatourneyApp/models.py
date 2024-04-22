from django.db import models

# Create your models here.
    
class Team(models.Model):
    team_ID = models.IntegerField()
    team_Name = models.CharField(max_length=30)
    wins = models.IntegerField()
    losses = models.IntegerField()
    team_Rank = models.IntegerField()
    objects = models.Manager()

    def getTeam_ID(self):
        return self.team_ID
    
    def getTeam_Name(self):
        return self.team_Name
    
    def getWins(self):
        return self.wins
    
    def getLosses(self):
        return self.losses
    
    def getTeam_Rank(self):
        return self.team_Rank
    
    def __str__(self):
        return self.team_ID + ": " + self.team_Name
    
class Moderator(models.Model):
    moderator_username=models.CharField(max_length=20,primary_key=True)
    moderator_password=models.CharField(max_length=20)
    objects = models.Manager()

    def getModeratorUsername(self):
        return self.moderator_username
    
    def getModeratorPassword(self):
        return self.moderator_password
    
    def __str__(self):
        return self.moderator_username
    
class Player(models.Model):
    player_ID=models.AutoField(primary_key=True)
    player_in_game_name=models.CharField(max_length=20, blank=True, null=True)
    player_fname=models.CharField(max_length=20, blank=True, null=True)
    player_lname=models.CharField(max_length=20, blank=True, null=True)
    player_dc_id=models.CharField(max_length=15, blank=True, null=True)
    player_fc=models.CharField(max_length=14, blank=True, null=True)
    player_rank=models.CharField(max_length=5, blank=True, null=True)
    player_role=models.CharField(max_length=10, blank=True, null=True)
    player_type=models.CharField(max_length=10, default="member", null=True)
    player_checkin_status=models.CharField(max_length=20, blank=True, null=True)
    objects = models.Manager()
    Team_ID = models.ForeignKey(Team, blank=True, null=True, on_delete=models.CASCADE)    


    def getPlayer_ID(self):
        return self.player_ID
    
    def getPlayer_in_game_name(self):
        return self.player_in_game_name
    
    def getPlayerFullName(self):
        return f'{self.player_fname} {self.player_lname}'

    def getPlayerFirstName(self):
        return self.player_fname
    
    def getPlayerLastName(self):
        return self.player_lname
    
    def getPlayerDiscordID(self):
        return self.player_dc_id
    
    def getPlayerFriendCode(self):
        return self.player_fc
    
    def getPlayerRank(self):
        return self.player_rank
    
    def getPlayerRole(self):
        return self.player_role
    
    def getPlayerType(self):
        return self.player_type
    
    def __str__(self):
        return self.player_ID + ": " + self.player_in_game_name
    
class PlayerRole(models.Model):
    player_ID = models.ForeignKey(Player, on_delete=models.CASCADE)
    player_role = models.CharField(max_length=20)
    object = models.Manager()

    def __str__(self):
        return self.player_ID + ": " + self.player_role

class Tournament(models.Model):
    tournament_title = models.CharField(max_length=60, primary_key=True)
    tournament_description = models.CharField(max_length=300)
    tournament_mode = models.CharField(max_length=6)
    registration_status = models.CharField(max_length=18)
    tournament_status = models.CharField(max_length=12)
    objects = models.Manager()

    def getTournamentTitle(self):
        return self.tournament_title
    
    def getTournamentDescription(self):
        return self.tournament_description
    
    def getTournamentMode(self):
        return self.tournament_mode
    
    def getRegistrationStatus(self):
        return self.registration_status
    
    def getTournamentStatus(self):
        return self.tournament_status

    def __str__(self):
        return self.tournament_title

class Bracket(models.Model):
    tournament_title = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    bracket_ID = models.IntegerField()
    bracket_Name = models.CharField(max_length=20)
    objects = models.Manager()

    def getBracket_ID(self):
        return self.bracket_ID
    
    def getBracket_Name(self):
        return self.bracket_Name
    
    def __str__(self):
        return self.bracket_ID + ": " + self.bracket_Name

class BracketColumn(models.Model):
    bracket_ID = models.ForeignKey(Bracket, on_delete=models.CASCADE)
    bracketColumn_ID = models.IntegerField()
    bracketColumn_Name = models.CharField(max_length=20)
    bracketColumn_Limit = models.IntegerField()
    objects = models.Manager()

    def getBracketColumn_Name(self):
        return self.bracketColumn_Name
    
    def getBracketColumn_Limit(self):
        return self.bracketColumn_Limit
    
    def __str__(self):
        return self.bracketColumn_ID + ": " + self.bracketColumn_Name

class Pairing(models.Model):
    bracketColumn_ID = models.ForeignKey(BracketColumn, on_delete=models.CASCADE)
    pairing_ID = models.IntegerField()
    pairing_Name = models.CharField(max_length=20)
    pairing_Status = models.CharField(max_length=11)
    objects = models.Manager()

    def getPairing_Name(self):
        return self.pairing_Name
    
    def getPairing_Status(self):
        return self.pairing_Status
    
    def __str__(self):
        return self.pairing_ID + ": " + self.pairing_Name

class GameEntry(models.Model):
    team_ID = models.ForeignKey(Team, on_delete=models.CASCADE)
    pairing_ID = models.ForeignKey(Pairing, on_delete=models.CASCADE)
    team_Check_in_Status = models.CharField(max_length=11)
    game_Result = models.CharField(max_length=4)
    objects = models.Manager()

    def getTeam_Check_in_Status(self):
        return self.pairing_ID

    def getGame_Result(self):
        return self.game_Result
    
class Schedule(models.Model):
    schedule_ID = models.IntegerField()
    time_Start = models.TimeField()
    time_End = models.TimeField()
    objects = models.Manager()