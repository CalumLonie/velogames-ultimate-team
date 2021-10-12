# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 16:19:06 2020

@author: Calum
"""

import csv

n_races = 2
n_riders = 6

def initialise (n_teams, default):
    set = []
    for d in range(n_teams):
        set.append(default)
    return set

def adding (info, rs, s, index, n_teams, col):
    rs_sub = initialise(n_teams, 0)
    for r in range(n_riders):
        rs_sub[r] = rs[r]
    rs_sub[index] = s
    sub = 0
    for r in rs_sub:
        sub += info[r][col]
        
    return sub

def order (info, rs, s, index):
    rs_inter = initialise(n_riders-1, 0)
    rs_sub = initialise(n_riders, 0)
    cost_to_sub = info[s][1]
    
    l = 0
    for r in range(n_riders):
        if r != index:
            rs_inter[l] = rs[r]
            l += 1
    
    for r in rs_inter:
        if cost_to_sub > info[r][1]:
            location = r
            break
    
    rs_sub[0:location] = rs_inter[0:location]
    rs_sub[location] = s
    rs_sub[location+1:n_riders] = rs_inter[location+1:n_riders-1]
    
    sub = initialise(n_riders, 0)
    for r in range(n_riders):
        sub[r] = info[rs_sub[r]][0]
        
    return sub

def new_team (info, rs, s, index):
    sub = [info[rs[0]][0], info[rs[1]][0], info[rs[2]][0], info[rs[3]][0], info[rs[4]][0], info[rs[5]][0]]
    sub[index] = info[s][0]
    return sub

in_file = open('Squad_Test.txt', 'r')
info = []
l = 0

data = csv.DictReader(in_file)
for row in data:
    info.append(row)
    info[l]['Cost'] = int(info[l]['Cost'])
    info[l]['Race1'] = int(info[l]['Race1'])
    info[l]['Race2'] = int(info[l]['Race2'])
    info[l]['Total'] = int(info[l]['Total'])
    l += 1
in_file.close()

n_all = len(info)

info_race1 = []
info_race2 = []

for row in range(n_all):
    info_race1.append([info[row]['Names'], info[row]['Cost'], info[row]['Race1']])
    info_race2.append([info[row]['Names'], info[row]['Cost'], info[row]['Race2']])
    
squad_teams = initialise(n_races, [])
squad_scores = initialise(n_races, 0)
comb_scores = initialise(n_races, 0)
squad_costs = initialise(n_races, 0)
comb_costs = initialise(n_races, 0)
squad_total = 0

for r1 in range(n_all-5):
    print(r1)
    for r2 in range(r1+1,n_all-4):
        for r3 in range(r2+1,n_all-3):
            for r4 in range(r3+1,n_all-2):
                for r5 in range(r4+1,n_all-1):
                    for r6 in range(r5+1,n_all):
                        rs = [r1, r2, r3, r4, r5, r6]
                        comb_costs[0] = info_race1[r1][1] + info_race1[r2][1] + info_race1[r3][1] + info_race1[r4][1] + info_race1[r5][1] + info_race1[r6][1]
                        if comb_costs[0] <= 56:
                            comb_scores[0] = info_race1[r1][2] + info_race1[r2][2] + info_race1[r3][2] + info_race1[r4][2] + info_race1[r5][2] + info_race1[r6][2]
                            score_nosub = info_race2[r1][2] + info_race2[r2][2] + info_race2[r3][2] + info_race2[r4][2] + info_race2[r5][2] + info_race2[r6][2]
                            if comb_scores[0] + score_nosub > squad_total:
                                squad_teams[0] = [info_race1[r1][0], info_race1[r2][0], info_race1[r3][0], info_race1[r4][0], info_race1[r5][0], info_race1[r6][0]]
                                squad_teams[1] = squad_teams[0]
                                squad_scores[0] = comb_scores[0]
                                squad_scores[1] = score_nosub
                                squad_costs[0] = comb_costs[0]
                                squad_costs[1] = squad_costs[0]
                                squad_total = squad_scores[0] + squad_scores[1]
                            for s in range(n_all):
                                if s != r1 and s != r2 and s != r3 and s != r4 and s != r5 and s != r6:
                                    for rider in range(n_riders):
                                        cost_sub = adding(info_race2, rs, s, rider, n_riders, 1)
                                        if cost_sub <= 56:
                                            score_sub = adding(info_race2, rs, s, rider, n_riders, 2)
                                            if comb_scores[0] + score_sub > squad_total:
                                                squad_teams[0] = [info_race1[r1][0], info_race1[r2][0], info_race1[r3][0], info_race1[r4][0], info_race1[r5][0], info_race1[r6][0]]
                                                squad_teams[1] = new_team(info_race2, rs, s, rider)
                                                squad_scores[0] = comb_scores[0]
                                                squad_scores[1] = score_sub
                                                squad_costs[0] = comb_costs[0]
                                                squad_costs[1] = cost_sub
                                                squad_total = squad_scores[0] + squad_scores[1]
                                                
print('Evaluation of all combinations complete.')

out_file = open('Squad_Test_US.txt', 'w')

out_file.write('The Ultimate Squad scored ' + str(squad_total) + ' points.' + '\n' + '\n')
for race in range(n_races):
    out_file.write('The team for Race ' + str(race + 1) + ' was:' + '\n')
    for rider in range(n_riders):
        out_file.write(str(squad_teams[race][rider]) + '\n')
    out_file.write('Scoring ' + str(squad_scores[race]) + ' points.' + '\n')
    out_file.write('Costing ' + str(squad_costs[race]) + ' credits.' + '\n' + '\n')

out_file.close()