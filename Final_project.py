total_games = 0
total_wins = 0
total_breaks = 0
total_broken = 0
total_errors = 0
total_serves = 0
total_serves_made = 0
total_serves_missed = 0
total_double_faults = 0
total_aces = 0
total_aced = 0
total_hits = 0
total_hitting_errors = 0
total_put_aways = 0
total_hits_missed = 0
total_hits_on = 0
total_hits_returned = 0
total_sets = 0
total_strong_sets = 0
total_weak_sets = 0
total_set_errors = 0
total_defensive_touches = 0
total_strong_plays = 0
total_weak_plays = 0

while True:
    tournament_games = 0
    tournament_wins = 0
    tournament_breaks = 0
    tournament_broken = 0
    tournament_errors = 0
    tournament_serves = 0
    tournament_serves_made = 0
    tournament_serves_missed = 0
    tournament_double_faults = 0
    tournament_aces = 0
    tournament_aced = 0
    tournament_hits = 0
    tournament_hitting_errors = 0
    tournament_put_aways = 0
    tournament_hits_missed = 0
    tournament_hits_on = 0
    tournament_hits_returned = 0
    tournament_sets = 0
    tournament_strong_sets = 0
    tournament_weak_sets = 0
    tournament_set_errors = 0
    tournament_defensive_touches = 0
    tournament_strong_plays = 0
    tournament_weak_plays = 0

    games = input("Please enter the number of games played: ")
    games_int = int(games)
    total_games += games_int
    tournament_games += games_int

    while True:
        print("\nIf you would like to quit at anytime, please enter 'q'!")
        print("\nFirst, let's take a look at how you served the ball!")   #ask user for input about serves
        serves_made_stat = input("Please enter the number of serves made: ")    #ask user for input about serves made
        if serves_made_stat.lower() == "q":
            break
        smds = int(serves_made_stat)
        total_serves_made += smds
        total_serves += smds
        tournament_serves_made += smds
        tournament_serves += smds
        
        serves_missed_stat = input("Please enter the number of serves missed: ")    #ask user for input about serves missed
        if serves_missed_stat.lower() == "q":
            break
        smss = int(serves_missed_stat)
        total_serves_missed += smss
        total_serves += smss
        tournament_serves_missed += smss
        tournament_serves += smss

        double_faults_stat = input("Please enter the number of double faults: ")    #ask user for input about double faults
        if double_faults_stat.lower() == "q":
            break
        dfs = int(double_faults_stat)
        total_double_faults += dfs
        tournament_double_faults += dfs 

        aces_stat = input("Please enter the number of aces: ")  #ask user for input about aces
        if aces_stat.lower() == "q":
            break
        acs = int(aces_stat)
        total_aces += acs
        tournament_aces += acs

        print("\nNow let's take a look at how you did at hitting!") #ask user for input about hitting
        hits_on_stat = input("Please enter the number of times you hit the ball onto the net: ")    #ask user for input about hits made onto the net
        if hits_on_stat.lower() == "q":
            break
        hos = int(hits_on_stat)
        total_hits_on += hos
        total_hits += hos
        tournament_hits_on += hos 
        tournament_hits += hos

        hits_missed_stat = input("Please enter the number of hits that missed the net: ")   #ask user for input about hits that missed the net
        if hits_missed_stat.lower() == "q":
            break
        hms = int(hits_missed_stat)
        total_hits_missed += hms
        total_hits += hms
        tournament_hits_missed += hms 
        tournament_hits += hms

        hitting_error_stat = input("Please enter the number of hitting errors made: ")  #ask user for input about hitting errors
        if hitting_error_stat.lower() == "q":
            break
        hes = int(hitting_error_stat)
        total_hitting_errors += hes
        tournament_hitting_errors += hes 

        hits_returned_stat = input("Please enter the numher of times one of your hits on the net was returned: ")
        hrs = int(hits_returned_stat)
        total_hits_returned += hrs
        tournament_hits_returned += hrs

        


