'''This script requires python 2.7, and gathers data from all years prior to 2019.'''

import nflgame
import pandas as pd
import numpy as np
import datetime
import os


cwd=(os.getcwd()+'\\').replace('\\','\\\\')
data_dir=cwd+'data\\\\'

pd.set_option('display.max_columns', None)


flag=True
while flag:
    week=int(raw_input('What week is complete (enter int between 1 and 16): '))
    print 'Week is :'.format(week)
    if isinstance(week,int) and (week>=1) and (week<=16):
        flag=False
        print 'Flag=: {}'.format(flag)

flag=True
while flag:
    partials=raw_input('Do you want partial weeks:')
    possible_answers=['YES','Yes','yes','Y','y',
                    'NO','No','no','N','n']
    if partials in possible_answers:
        flag=False

# Set up years list
start_time=datetime.datetime.now()

#years_list=range(2009,2019) #Convert to 2019
years_list=[2019]
print "Gathering data for: {}".format(' '.join([str(x) for x in years_list]))

all_years_data=pd.DataFrame()

# Loop through years'
for y in years_list:
    start_loop_time=datetime.datetime.now()
    print 'Year:{}'.format(y)
    games=nflgame.games(y)

    all_data=[]

    for g in games:
        columns=g.schedule.keys()
        all_data.append(g.schedule.values())

    # basic schedule info
    year_df=pd.DataFrame(columns=columns,data=all_data)

    try:
        year_df=year_df[['eid','year','week','month','day','wday','time',
            'meridiem','gamekey','home','away',
            'season_type']].sort_values('eid',ascending=True)
    except:
        year_df=year_df[['eid','year','week','month','day','wday','time',
            'gamekey','home','away',
            'season_type']].sort_values('eid',ascending=True)


    # basic scoring results
    g_columns=['eid','score_home','score_away',  'winner','loser','score_home_q1','score_home_q2',
        'score_home_q3','score_home_q4','score_home_q5','score_away_q1','score_away_q2',
        'score_away_q3','score_away_q4','score_away_q5','scores']

    all_data=[]
    for g in games:
        all_data.append([g.eid,g.score_home,g.score_away,g.winner,g.loser, g.score_home_q1,
            g.score_home_q2,g.score_home_q3,g.score_home_q4,g.score_home_q5,g.score_away_q1,
            g.score_away_q2,g.score_away_q3,g.score_away_q4,g.score_away_q5,g.scores])

    games_year_df=pd.DataFrame(columns=g_columns,data=all_data)
    game_data_df=pd.merge(year_df,games_year_df,how='left',on='eid')
    game_data_df=game_data_df.sort_values('eid')

    # team stats gets added
    team_stats=['first_downs','total_yds','passing_yds','rushing_yds','penalty_cnt','penalty_yds','turnovers','punt_cnt',
            'punt_yds','punt_avg','pos_time_tot_seconds']
    home_stats_n=['h_'+x for x in team_stats]
    away_stats_n=['a_'+x for x in team_stats]

    all_data=[]

    for g in games:

        home_stats=[g.stats_home.first_downs,
                    g.stats_home.total_yds,
                    g.stats_home.passing_yds,
                    g.stats_home.rushing_yds,
                    g.stats_home.penalty_cnt,
                    g.stats_home.penalty_yds,
                    g.stats_home.turnovers,
                    g.stats_home.punt_cnt,
                    g.stats_home.punt_yds,
                    g.stats_home.punt_avg,
                    g.stats_home.pos_time.total_seconds()]

        away_stats=[g.stats_away.first_downs,
                    g.stats_away.total_yds,
                    g.stats_away.passing_yds,
                    g.stats_away.rushing_yds,
                    g.stats_away.penalty_cnt,
                    g.stats_away.penalty_yds,
                    g.stats_away.turnovers,
                    g.stats_away.punt_cnt,
                    g.stats_away.punt_yds,
                    g.stats_away.punt_avg,
                    g.stats_away.pos_time.total_seconds()]

        game_line=[g.eid]+home_stats+away_stats
        all_data.append(game_line)

    stats_columns=['eid']+home_stats_n+away_stats_n
    team_stats_df=pd.DataFrame(columns=stats_columns,data=all_data).sort_values('eid')

    game_data_df=pd.merge(game_data_df,team_stats_df,how='left',on='eid')
    game_data_df=game_data_df.sort_values('eid')

    #Add some player info (ie: birthdate, experience, weight, height)
    player_info=['player_id','playerid','profile_id','last_name','first_name','position','height','weight','birthdate','years_pro']

    all_players=[]
    keys=nflgame.players.keys()
    for p in keys:
        p=nflgame.players[p]
        player=[p.player_id,p.playerid,p.profile_id,p.last_name,p.first_name,p.position,p.height,p.weight,
                p.birthdate,p.years_pro]
        all_players.append(player)

    players_df=pd.DataFrame(columns=player_info,data=all_players)
    players_df=players_df.rename(columns={'player_id':'id'})

    #get individual player stats for each game
    all_player_stats=pd.DataFrame()
    for g in games:
        g.players.csv('player-stats.csv')
        player_stats=pd.read_csv('player-stats.csv')
        player_stats['eid']=g.eid
        mstats=nflgame.combine_max_stats([g])
        mstats.csv('my_stats.csv',True)
        my_stats=pd.read_csv('my_stats.csv')
        new_col=['id']+list(set(my_stats.columns).difference(set(player_stats.columns)))
        my_stats=my_stats[new_col]
        player_stats=pd.merge(player_stats,my_stats,on='id')

        all_player_stats=all_player_stats.append(player_stats)


    big_df=pd.merge(all_player_stats,game_data_df,how='left',on='eid')
    big_df=pd.merge(big_df,players_df,how='left',on='id')
    big_df.to_csv('player_data_b_{}.csv'.format(y))

    all_years_data=all_years_data.append(big_df)
    #all_years_data.to_csv('player_data_2009_2018.csv') #Update to 2019
    all_years_data.to_csv('player_data_b_2019.csv')
    all_years_data.to_csv(data_dir+'player_data_b_2019.csv')

    print 'Complete year: {}'.format(y)
    year_time=((datetime.datetime.now()-start_loop_time).total_seconds())/60.0
    total_time=((datetime.datetime.now()-start_time).total_seconds())/60.0
    print 'Year took {:0.2f} minutes, total elapsed time: {:0.2f} minutes'\
    .format(year_time,total_time)

previous_years=pd.read_csv(data_dir+'player_data_2009_2018.csv')
print 'Length previous years data: {} length of {}: {}'.format(len(previous_years),y,
        len(big_df)),
previous_years=previous_years.append(big_df)
previous_years.to_csv(data_dir+'data_2009_present.csv')
print 'Len present data: {}'.format(len(previous_years))
print 'Done'
