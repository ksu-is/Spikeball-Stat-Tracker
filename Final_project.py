def spikeball():
    total_games = 0 
    total_wins = 0 
    total_losses = 0 
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
    total_weak_hits = 0
    total_hits_returned = 0 
    total_sets = 0 
    total_strong_sets = 0 
    total_weak_sets = 0 
    total_set_errors = 0 
    total_defensive_touches = 0 
    total_strong_defensive_touches = 0
    total_weak_defensive_touches = 0
    total_strong_recieves = 0 
    total_weak_recieves = 0 
    total_strong_plays = 0 
    total_weak_plays = 0

    while True:
        tournament_games = 0
        tournament_wins = 0
        tournaments_losses = 0
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
        tournament_weak_hits = 0
        tournament_hits_returned = 0
        tournament_sets = 0
        tournament_strong_sets = 0
        tournament_weak_sets = 0
        tournament_set_errors = 0
        tournament_defensive_touches = 0
        tournament_strong_defensive_touches = 0
        tournament_weak_defensive_touches = 0
        tournament_strong_recieves = 0
        tournament_weak_recieves = 0
        tournament_strong_plays = 0
        tournament_weak_plays = 0

        games = input("Please enter the number of games played: ")  #ask user for input about number of games played
        games_int = int(games)
        total_games += games_int
        tournament_games += games_int

        while True:
            print("\nIf you would like to quit at anytime, please enter 'q'!")
            print("\nFirst, let's take a look at how you served the ball!")   #ask user for input about serves
            serves_made_stat = input("Please enter the number of serves made: ")    #ask user for input about serves made
            if serves_made_stat.lower() == "q":
                break
            else:
                smds = int(serves_made_stat)
                total_serves_made += smds
                total_serves += smds
                tournament_serves_made += smds
                tournament_serves += smds
            
            serves_missed_stat = input("Please enter the number of serves missed: ")    #ask user for input about serves missed
            if serves_missed_stat.lower() == "q":
                break
            else:
                smss = int(serves_missed_stat)
                total_serves_missed += smss
                total_serves += smss
                tournament_serves_missed += smss
                tournament_serves += smss

            double_faults_stat = input("Please enter the number of double faults: ")    #ask user for input about double faults
            if double_faults_stat.lower() == "q":
                break
            else:
                dfs = int(double_faults_stat)
                total_double_faults += dfs
                tournament_double_faults += dfs 

            aces_stat = input("Please enter the number of aces: ")  #ask user for input about aces
            if aces_stat.lower() == "q":
                break
            else:
                acs = int(aces_stat)
                total_aces += acs
                tournament_aces += acs

            print("\nNow let's take a look at how you did at hitting!") #ask user for input about hitting
            hits_on_stat = input("Please enter the number of times you hit the ball onto the net: ")    #ask user for input about hits made onto the net
            if hits_on_stat.lower() == "q":
                break
            else:
                hos = int(hits_on_stat)
                total_hits_on += hos
                total_hits += hos
                tournament_hits_on += hos 
                tournament_hits += hos

            put_aways_stat = input("Please enter the number of times you put the ball away: ")  #asks user about number of put aways
            if put_aways_stat.lower() == "q":
                break
            else:
                pas = int(put_aways_stat)
                total_put_aways += pas
                tournament_put_aways += pas

            weak_hits_stat = input("Please enter the number of weak hits you made: ")
            if weak_hits_stat.lower() == "q":
                break
            else:
                whs = int(weak_hits_stat)
                total_weak_hits += whs
                tournament_weak_hits += whs

            hits_missed_stat = input("Please enter the number of hits that missed the net: ")   #ask user for input about hits that missed the net
            if hits_missed_stat.lower() == "q":
                break
            else:
                hms = int(hits_missed_stat)
                total_hits_missed += hms
                total_hits += hms
                tournament_hits_missed += hms 
                tournament_hits += hms

            hitting_error_stat = input("Please enter the number of hitting errors made: ")  #ask user for input about hitting errors
            if hitting_error_stat.lower() == "q":
                break
            else:
                hes = int(hitting_error_stat)
                total_hitting_errors += hes
                total_errors += hes
                tournament_hitting_errors += hes 
                tournament_errors += hes

            hits_returned_stat = input("Please enter the numher of times one of your hits on the net was returned: ")   #ask for user input about hits returned
            if hits_returned_stat.lower() == "q":
                break
            else:
                hrs = int(hits_returned_stat)
                total_hits_returned += hrs
                tournament_hits_returned += hrs

            print("\nNow let's take a look at how you did setting!")    #ask user about setting
            strong_sets_stat = input("Please enter the number of strong sets you made: ")   #ask user about number of strong sets made
            if strong_sets_stat.lower() == "q":
                break
            else:
                sss = int(strong_sets_stat)
                total_strong_sets += sss
                total_sets += sss
                tournament_strong_sets += sss
                tournament_sets += sss

            weak_set_stats = input("Please enter the number of weak sets you made: ")   #ask user about number of weak sets made
            if weak_set_stats.lower() == "q":
                break
            else:
                wss = int(weak_set_stats)
                total_weak_sets += wss
                total_sets += wss
                tournament_weak_sets += wss
                tournament_sets += wss

            setting_errors_stat = input("Please enter the number of setting errors you made: ")    #ask user about number of setting errors made
            if setting_errors_stat.lower() == "q":
                break
            else:
                ses = int(setting_errors_stat)
                total_set_errors += ses
                total_errors += ses
                tournament_set_errors += ses
                tournament_errors += ses

            print("\nNow let's take a look at your defense!")   #asks user about defense
            defensive_touches_stat = input("Please enter the number of defensive touches you made: ")    #asks user about number of defensive touches made
            if defensive_touches_stat.lower() == "q":
                break
            else:
                dts = int(defensive_touches_stat)
                total_defensive_touches += dts
                tournament_defensive_touches += dts

            strong_defensive_touches_stat = input("Please enter the total number of strong defensive touches you made: ")  #asks user about number of strong defensive touches made
            if strong_defensive_touches_stat.lower() =="q":
                break
            else:
                sdts = int(strong_defensive_touches_stat)
                total_strong_defensive_touches += sdts
                tournament_strong_defensive_touches += sdts

            weak_defensive_touches_stat = input("Please enter the number of weak defensive touches you made: ") #asks user about number of weak defensive touches made
            if weak_defensive_touches_stat.lower() == "q":
                break
            else:
                wdts = int(weak_defensive_touches_stat)
                total_weak_defensive_touches += wdts
                tournament_weak_defensive_touches += wdts

            aced_stat = input("Please enter the number of times you were aced: ")   #asks user about number of times aced
            if aces_stat.lower() == "q":
                break
            else:
                acds = int(aced_stat)
                total_aced += acds
                tournament_aced += acds

            strong_recieve_stat = input("Please enter the number of strong recieves you made: ")    #asks user about number of strong recieves
            if strong_recieve_stat.lower() == "q":
                break
            else:
                srs = int(strong_recieve_stat)
                total_strong_recieves += srs
                tournament_strong_recieves += srs
            
            weak_recieve_stat = input("Please enter the number of weak recieves: ")     #asks user about number of weak recieves
            if weak_recieve_stat.lower() == "q":
                break
            else:
                wrs = int(weak_recieve_stat)
                total_weak_recieves += wrs
                tournament_weak_recieves += wrs

            print("\nFinally, let's take a look at your points and games as a whole!")  #asks user about points and games as a whole
            breaks_stat = input("Please enter the number of breaks you had: ")  #asks user about number of breaks
            if breaks_stat.lower() == "q":
                break
            else:
                bks = int(breaks_stat)
                total_breaks += bks
                tournament_breaks += bks

            broken_stat = input("Please enter the number of times you were broken: ")   #asks user about number of times user was broken
            if broken_stat.lower() == "q":
                break
            else:
                bkns = int(broken_stat)
                total_broken += bkns
                tournament_broken += bkns

            games_won_stat = input("Please enter the number of games you won: ")    #asks user about number of games won
            if games_won_stat.lower() == "q":
                break
            else:
                gws = int(games_won_stat)
                total_wins += gws
                tournament_wins += gws

            break

        total_losses = total_games - total_wins #calculate number of games lost using total games and games won
        tournaments_losses = tournament_games - tournament_wins

        total_serves_made_percent = total_serves_made / total_serves * 100  #calculates percentage of serves made
        tournament_serves_made_percent = tournament_serves_made / tournament_serves * 100

        total_hits_made_percent = total_hits_on / total_hits * 100  #calculates percentage of hits made 
        tournament_hits_made_percent = tournament_hits_on / tournament_hits * 100

        total_strong_plays = total_strong_recieves + total_strong_sets + total_put_aways + total_strong_defensive_touches   #calculates number of strong plays
        tournament_strong_plays = tournament_strong_recieves + tournament_strong_sets + tournament_put_aways + tournament_strong_defensive_touches

        total_weak_plays = total_weak_recieves + total_weak_sets + total_weak_hits + total_weak_defensive_touches   #calculates number of weak plays
        tournament_weak_plays = tournament_weak_recieves + tournament_weak_sets +tournament_weak_hits + tournament_weak_defensive_touches

        total_hitting_spr = 20 - (20 * total_hits_returned / total_hits)    #calculates hitting spikeball player rating
        tournament_hitting_spr = 20 - (20 *tournament_hits_returned / tournament_hits)

        total_defense_spr = .4 * total_hitting_spr * total_strong_defensive_touches + total_weak_defensive_touches  #calculates defense spikeball player rating
        tournament_defense_spr = .4 * tournament_hitting_spr * tournament_strong_defensive_touches + tournament_weak_defensive_touches

        total_efficiency_spr = 20 - 5 * total_errors - 2 * (total_weak_plays + total_aced)  #calculates efficiency spikeball player rating
        tournament_efficiency_spr = 20 - 5 * tournament_errors - 2 * (tournament_weak_plays + tournament_aced)

        total_serving_spr = 5.5 * total_aces + 15 * (total_serves_made / total_serves)  #calculates serving spikeball player rating
        tournament_serving_spr = 5.5 * tournament_aces + 15 * (tournament_serves_made / tournament_serves)

        total_spr = 1.57 * (total_hitting_spr + total_defense_spr + total_serving_spr + total_efficiency_spr)   #calculates total spikeball player rating
        tournament_spr = 1.57 * (tournament_hitting_spr + total_defense_spr + tournament_serving_spr + total_efficiency_spr)

        break

    print("\n\nLet's take a look at your stats from this tournament!")
    print("\nServing: \n\tTotal serves:", tournament_serves, "\n\tServes made:", tournament_serves_made, "\n\tServes missed:", tournament_serves_missed, "\n\tDouble faults:", tournament_double_faults, "\n\tAces:", tournament_aces, "\n\tServing percentage:", tournament_serves_made_percent, "%")    #gives user info about their serving
    if tournament_serves_made_percent > total_serves_made_percent:
        print("\n\tCongrats! Your serving percentage this tournament is better than your average serving percentage!")
    else:
        print("\n\tYour serving percentage isn't quite up to your average serving percentage. That may be something you want to work on!\n")

    print("\nHitting: \n\tTotal hits:", tournament_hits, "\n\tHits on net:", tournament_hits_on, "\n\tHits missed:", tournament_hits_missed, "\n\tPut aways:", tournament_put_aways, "\n\tWeak hits:", tournament_weak_hits, "\n\tHitting errors:", tournament_hitting_errors, "\n\tHitting percentage:", tournament_hits_made_percent, "%")    #gives user info about hitting
    if tournament_hits_made_percent > total_hits_made_percent:
        print("\n\tCongrats! Your hitting percentage this tournament is better than your average hitting percentage!")
    else:
        print("\n\tYour hitting percentage isn't quite up to your average hitting percentage. That may need to be something you need to work on!\n")

    print("\nSetting: \n\tTotal sets:", tournament_sets, "\n\tStrong sets:", tournament_strong_sets, "\n\tWeak sets:", tournament_weak_sets, "\n\tSetting Errors :", tournament_set_errors) #gives user info about setting
    if tournament_set_errors < total_set_errors:
        print("\n\tCongrats! Your setting this tournament is better than what your average is!\n")
    else:
        print("\n\tYour setting isn't quite up to your average. That may be something you want to work on!\n")  

    print("\nDefense: \n\tDefensive touches:", tournament_defensive_touches, "\n\tStrong defensive touches:", tournament_strong_defensive_touches, "\n\tWeak defensive touches:", tournament_weak_defensive_touches, "\n\tNumber of times aced:", tournament_aced, "\n\tStrong receives:", tournament_strong_recieves, "\n\tWeak receives:", tournament_weak_recieves)  #gives user info about defense
    if tournament_defense_spr < total_serving_spr:
        print("\n\tCongrats! Your defense is better than what it usually is!\n")
    else:
        print("\n\tYour defense ins't quite what it normally is. That might be something you want to work on!\n")

    print("\nTotals:\n\tTotal games:", tournament_games, "\n\tGames won:", tournament_wins, "\n\tGames lost:", tournaments_losses, "\n\tTotal breaks:", tournament_breaks, "\n\tTotal broken:", tournament_broken, "\n\tErrors:", tournament_errors, "\n\tStrong plays:", tournament_strong_plays, "\n\tWeak plays:", tournament_weak_plays, "\n")  #gives user info about totals

    print("\nSPR's: \n\tHitting:", tournament_hitting_spr, "\n\tDefense:", tournament_defense_spr, "\n\tEfficiency:", tournament_efficiency_spr, "\n\tServing:", tournament_serving_spr, "\n\tTotal:", tournament_spr)   #gives user info about different SPR's

    print("\n\n\nNow let's take a look at your total stats including this tournament!")

    print("\nServing: \n\tTotal serves:", total_serves, "\n\tServes made:", total_serves_made, "\n\tServes missed:", total_serves_missed, "\n\tDouble faults:", total_double_faults, "\n\tAces:", total_aces, "\n\tServing percentage:", total_serves_made_percent, "%")    #gives user info about their serving

    print("\nHitting: \n\tTotal hits:", total_hits, "\n\tHits on net:", total_hits_on, "\n\tHits missed:", total_hits_missed, "\n\tPut aways:", total_put_aways, "\n\tWeak hits:", total_weak_hits, "\n\tHitting errors:", total_hitting_errors, "\n\tHitting percentage:", total_hits_made_percent, "%")    #gives user info about hitting

    print("\nSetting: \n\tTotal sets:", total_sets, "\n\tStrong sets:", total_strong_sets, "\n\tWeak sets:", total_weak_sets, "\n\tSetting Errors :", total_set_errors) #gives user info about setting

    print("\nDefense: \n\tDefensive touches:", total_defensive_touches, "\n\tStrong defensive touches:", total_strong_defensive_touches, "\n\tWeak defensive touches:", total_weak_defensive_touches, "\n\tNumber of times aced:", total_aced, "\n\tStrong receives:", total_strong_recieves, "\n\tWeak receives:", total_weak_recieves)  #gives user info about defense

    print("\nTotals:\n\tTotal games:", total_games, "\n\tGames won:", total_wins, "\n\tGames lost:", total_losses, "\n\tTotal breaks:", total_breaks, "\n\tTotal broken:", total_broken, "\n\tErrors:", total_errors, "\n\tStrong plays:", total_strong_plays, "\n\tWeak plays:", total_weak_plays)  #gives user info about totals

    print("\nSPR's: \n\tHitting:", total_hitting_spr, "\n\tDefense:", total_defense_spr, "\n\tEfficiency:", total_efficiency_spr, "\n\tServing:", total_serving_spr, "\n\tTotal:", total_spr)   #gives user info about different SPR's

spikeball()

while True:
    cont = input("Would you like to add stats from another tournament? Y or N: ")   #asks if user would like to add stats from another tournament
    if cont.lower() == "y":
        spikeball()
    elif cont.lower() == "n":
        break
    else:
        print("Please enter a valid input")