from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def login(request):
    return render(request,'SplatourneyApp/tournament_details.html')   

def login_player(request):
    return render(request,'SplatourneyApp/tournament_details.html')

def login_moderator(request):
    if(request.method=="POST"):
        mod_name=request.POST.get("mod_name")
        mod_password=request.POST.get("mod_password")
        currentuser = Moderator.objects.filter(moderator_username=mod_name,moderator_password=mod_password)
        if not currentuser:
            return render(request, 'SplatourneyApp/login_moderator.html')
        else:
            return redirect('tournaments_screen')
    else:
        return render(request, 'SplatourneyApp/login_moderator.html')

def tournament_details(request):
    return render(request,'SplatourneyApp/tournament_details.html')
  
def player_registration(request):
    if(request.method=="POST"):
        p1_fname=request.POST.get("p1fname")
        p1_lname=request.POST.get("p1lname")
        p1_in_game_name=request.POST.get("p1ign")
        p1_dc_id=request.POST.get("p1dc")
        p1_fc=request.POST.get("p1fc")
        p1_rank=request.POST.get("p1rank")
        p1_role=request.POST.get("p1role")
        p1_type=request.POST.get("p1type")
        Player.objects.create(player_fname=p1_fname, player_lname=p1_lname, player_in_game_name=p1_in_game_name, player_dc_id=p1_dc_id, player_fc=p1_fc, player_rank=p1_rank, player_role=p1_role, player_type=p1_type)
        return redirect("view_registrations")    
    else:
        return render(request, 'SplatourneyApp/player_registration.html') 

def registration_type(request):
    return render(request,'SplatourneyApp/registration_type.html')

def team_registration(request):
    if (request.method=="POST"):
        team_Name = request.POST.get('Team_Name')
        Team.objects.create(team_ID=1, team_Name=team_Name, wins=0, losses=0, team_Rank=8)
        p1_fname=request.POST.get("p1fname")
        p1_lname=request.POST.get("p1lname")
        p1_in_game_name=request.POST.get("p1ign")
        p1_dc_id=request.POST.get("p1dc")
        p1_fc=request.POST.get("p1fc")
        p1_rank=request.POST.get("p1rank")
        p1_role=request.POST.get("p1role")
        p1_type=request.POST.get("p1type")
        Player.objects.create(team_ID=Team.objects.get(team_Name=team_Name).pk, player_fname=p1_fname, player_lname=p1_lname, player_in_game_name=p1_in_game_name, player_dc_id=p1_dc_id, player_fc=p1_fc, player_rank=p1_rank, player_role=p1_role, player_type=p1_type)
        p2_fname=request.POST.get("p2fname")
        p2_lname=request.POST.get("p2lname")
        p2_in_game_name=request.POST.get("p2ign")
        p2_dc_id=request.POST.get("p2dc")
        p2_fc=request.POST.get("p2fc")
        p2_rank=request.POST.get("p2rank")
        p2_role=request.POST.get("p2role")
        p2_type=request.POST.get("p2type")
        Player.objects.create(team_ID=Team.objects.get(team_Name=team_Name).pk, player_fname=p2_fname, player_lname=p2_lname, player_in_game_name=p2_in_game_name, player_dc_id=p2_dc_id, player_fc=p2_fc, player_rank=p2_rank, player_role=p2_role, player_type=p2_type)
        p3_fname=request.POST.get("p3fname")
        p3_lname=request.POST.get("p3lname")
        p3_in_game_name=request.POST.get("p3ign")
        p3_dc_id=request.POST.get("p3dc")
        p3_fc=request.POST.get("p3fc")
        p3_rank=request.POST.get("p3rank")
        p3_role=request.POST.get("p3role")
        p3_type=request.POST.get("p3type")
        Player.objects.create(team_ID=Team.objects.get(team_Name=team_Name).pk, player_fname=p3_fname, player_lname=p3_lname, player_in_game_name=p3_in_game_name, player_dc_id=p3_dc_id, player_fc=p3_fc, player_rank=p3_rank, player_role=p3_role, player_type=p3_type)
        p4_fname=request.POST.get("p4fname")
        p4_lname=request.POST.get("p4lname")
        p4_in_game_name=request.POST.get("p4ign")
        p4_dc_id=request.POST.get("p4dc")
        p4_fc=request.POST.get("p4fc")
        p4_rank=request.POST.get("p4rank")
        p4_role=request.POST.get("p4role")
        p4_type=request.POST.get("p4type")
        Player.objects.create(team_ID=Team.objects.get(team_Name=team_Name).pk, player_fname=p4_fname, player_lname=p4_lname, player_in_game_name=p4_in_game_name, player_dc_id=p4_dc_id, player_fc=p4_fc, player_rank=p4_rank, player_role=p4_role, player_type=p4_type)
        p5_fname=request.POST.get("p5fname")
        p5_lname=request.POST.get("p5lname")
        p5_in_game_name=request.POST.get("p5ign")
        p5_dc_id=request.POST.get("p5dc")
        p5_fc=request.POST.get("p5fc")
        p5_rank=request.POST.get("p5rank")
        p5_role=request.POST.get("p5role")
        p5_type=request.POST.get("p5type")
        Player.objects.create(team_ID=Team.objects.get(team_Name=team_Name).pk, player_fname=p5_fname, player_lname=p5_lname, player_in_game_name=p5_in_game_name, player_dc_id=p5_dc_id, player_fc=p5_fc, player_rank=p5_rank, player_role=p5_role, player_type=p5_type)
        p6_fname=request.POST.get("p6fname")
        p6_lname=request.POST.get("p6lname")
        p6_in_game_name=request.POST.get("p6ign")
        p6_dc_id=request.POST.get("p6dc")
        p6_fc=request.POST.get("p6fc")
        p6_rank=request.POST.get("p6rank")
        p6_role=request.POST.get("p6role")
        p6_type=request.POST.get("p6type")
        Player.objects.create(team_ID=Team.objects.get(team_Name=team_Name).pk, player_fname=p6_fname, player_lname=p6_lname, player_in_game_name=p6_in_game_name, player_dc_id=p6_dc_id, player_fc=p6_fc, player_rank=p6_rank, player_role=p6_role, player_type=p6_type)
    else:
        return render(request, 'SplatourneyApp/team_registration.html')
    
def view_registrations(request):
    Player_objects = Player.objects.all()
    return render(request, 'SplatourneyApp/registrations.html', {'Player': Player_objects})

def login_page(request):
    return render(request, 'SplatourneyApp/login_page.html')
  
def create_tournament(request):
    if request.method=="POST":
        tournament_title=request.POST.get("tournament_title")
        tournament_description=request.POST.get("tournament_description")
        tournament_mode=request.POST.get("tournament_mode")
        registration_status=request.POST.get("registration_status")
        tournament_status=request.POST.get("tournament_status")
        Tournament.objects.create(tournament_title=tournament_title, tournament_description=tournament_description, tournament_mode=tournament_mode, registration_status=registration_status, tournament_status=tournament_status)
        return redirect('tournament_details')
    else:
        return render(request, 'SplatourneyApp/create_tournament.html')

def edit_tournament(request, pk):
    if request.method=="POST":
        tournament_title=request.POST.get("tournament_title")
        tournament_description=request.POST.get("tournament_description")
        tournament_mode=request.POST.get("tournament_mode")
        registration_status=request.POST.get("registration_status")
        tournament_status=request.POST.get("tournament_status")
        Tournament.objects.filter(pk=pk).update(tournament_title=tournament_title, tournament_description=tournament_description, tournament_mode=tournament_mode, registration_status=registration_status, tournament_status=tournament_status)
        return redirect()
    else:
        return render ()

def pairings(request):
    pairing_objects = Pairing.objects.all()
    return render(request, '#', {'pairing': pairing_objects} )

def declare_winner(request):
    if request.method=='POST':
        winner = 'winner'
        Team.objects.filter(team_Name=winner).update(wins=+1)
    return render ('pairing_screens')

def start_tournament(request):
    #t = pk something something
    Tournament.objects.filter(pk='t').update(registration_status='Closed', tournament_status='ongoing')
    return redirect('tournament_details')

def create_bracket(request):                                                                                            #Function to create bracket
    Bracket.objects.create()                                                                                            
    total_team_count = 'total_team_count'                                                                               #Takes the total amount of teams
    counter = 1                                                                                                         #Divides the players by 8 (each bracket column will have 8 pairings)
    while counter < total_team_count:                                                                                   #loop to create bracket columns
        BracketColumn.objects.create(bracketColumn_Name='Column ' + counter, bracketColumn_limit=counter)
        counter = counter*2

def create_pairings(request):                                                                                           #Function to create pairings
    all_columns = BracketColumn.objects.all()                                                                           #Query to get a list of all bracket columns
    for x in all_columns:                                                                                               #Loop to make pairings in all bracket columns 
        column = BracketColumn.objects.get(pk=x)                                                                        #Get a specific bracket column using pk
        column_limit = column.bracketColumn_Limit                                                                       #Get the limit of the bracket column, to know when the loop stops making pairings
        column_id = column.pk                                                                                           #store in a variable
        for y in range(0, column_limit):                                                                                #Loop to make pairings based on the bracket column limit
            Pairing.objects.create(bracketColumn_ID=column_id, pairing_Name='Pairing ' + column_id + y, pairing_Status='Not Started')   #Creating the pairing

def create_starting_entries(request):                                                                                  #Function to create starting game entries for the teams (game entries for round 1)
    total_team_count = 'total_team_count'
    counter = 1                                                                                                        
    while counter < total_team_count:
           counter = counter*2
    start = BracketColumn.objects.get(bracketColumn_Limit=counter)                                                 
    start_ID = start.pk
    starting_pairings = Pairing.objects.all().filter(BracketColumn_ID=start_ID)
    teams = Team.objects.all()
    for x in starting_pairings:
        GameEntry.objects.create(pairing_ID=x)
        GameEntry.objects.create(pairing_ID=x)
    entries= GameEntry.objects.all()
    for y in teams:
        GameEntry.objects.filter()

    return
        
def create_tournament(request):
     return render(request, 'SplatourneyApp/create_tournament.html')
    
def pairing_screens(request):
    return render(request, 'SplatourneyApp/pairing_screens.html')

def create_team(request):
    if request.method=="POST":
        team_Name = 'team_Name'
        captain = 'captain'
        co_captain = 'co-captain'
        member1 = 'member1'
        member2 = 'member2'
        member3 = 'member3'
        member4 = 'member4'
        Player.objects.filter(player_in_game_name=captain).update(team_ID=Team.objects.get(team_Name=team_Name).pk, player_type='captain')
        Player.objects.filter(player_in_game_name=co_captain).update(team_ID=Team.objects.get(team_Name=team_Name).pk, player_type='co-captain')
        Player.objects.filter(player_in_game_name=member1).update(team_ID=Team.objects.get(team_Name=team_Name).pk)
        Player.objects.filter(player_in_game_name=member2).update(team_ID=Team.objects.get(team_Name=team_Name).pk)
        Player.objects.filter(player_in_game_name=member3).update(team_ID=Team.objects.get(team_Name=team_Name).pk)
        Player.objects.filter(player_in_game_name=member4).update(team_ID=Team.objects.get(team_Name=team_Name).pk)
        return redirect('view_registrations')
    else:
        return render(request, "SplatourneyApp/create_team.html")

def tournaments_screen(request):
    return render(request, 'SplatourneyApp/tournaments_screen.html')
