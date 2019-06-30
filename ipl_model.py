#!/usr/bin/env python
# coding: utf-8


import pandas as pd

players = pd.read_csv("/home/emkay/PycharmProjects/temp/cricket/ipl_players.csv" )

ipl_hist = pd.read_csv("/home/emkay/PycharmProjects/temp/cricket/deliveries.csv")

#
from fuzzywuzzy import fuzz 
from fuzzywuzzy import process 


# In[9]:


# PLAYER =[]
# TEAM = []
# for team in players.columns.tolist():
#     for val in players[team].values.tolist():
#         if process.extractOne(val,ipl_hist['batsman'].unique().tolist())[1] > 40:
#             PLAYER.append(process.extractOne(val,ipl_hist['batsman'].unique().tolist())[0])
#             TEAM.append(team)
# df = pd.DataFrame({"players":PLAYER,"team":TEAM})
#current_team = df.drop_duplicates()
#current_team['team'].unique()

current_team = pd.read_csv("/home/emkay/PycharmProjects/temp/cricket/team_ipl_2019.csv")
# match between srh x11p

print("Teams to be selected",current_team['team'].unique())

team1 = input("Enter team 1 \n")
print()
team2 = input("Enter team 2 \n")

team1 = current_team.loc[current_team['team']==team1]
team2 = current_team.loc[current_team['team']==team2]
the_team = pd.concat([team1,team2])
ipl_hist = ipl_hist[['batsman','non_striker','bowler','batsman_runs','player_dismissed','dismissal_kind','fielder']]
ipl_hist = ipl_hist.loc[(ipl_hist['batsman'].isin(the_team['players'])) & (ipl_hist['bowler'].isin(the_team['players']))]
ipl_hist = ipl_hist.fillna(0)
batsman = []
runs = []
for val in ipl_hist['batsman'].unique():
    batsman.append(val)
    runs.append(sum(ipl_hist.loc[ipl_hist['batsman']==val]['batsman_runs'].values.tolist()))
df_bt = pd.DataFrame({"Player":batsman,"Runs":runs}).sort_values(by=['Runs'],ascending=False)
print(df_bt)

codes = {'bowled':1, 'caught':1, 'retired hurt':0, 'run out':0, 'stumped':1,
       'caught and bowled':1, 'lbw':1, 'hit wicket':0}

ipl_hist['dismissal_kind'] = ipl_hist['dismissal_kind'].str.strip().map(codes)
ipl_hist = ipl_hist.fillna(0)
bowlers = []
wickets = []
for val in ipl_hist['bowler'].unique():
    bowlers.append(val)
    wickets.append(sum(ipl_hist.loc[ipl_hist['bowler']==val]['dismissal_kind'].values.tolist()))
df_bw = pd.DataFrame({"bowlers":bowlers,"wickets":wickets}).sort_values(by=['wickets'],ascending=False)
print(df_bw)


