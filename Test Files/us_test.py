# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 22:19:32 2020

@author: Calum
"""


import csv

race_name = 'Squad_Test'

n_riders = 6
n_subs = 3
gender = 'M'
max_cost = 54

def initialise (n_teams, default):
    set = []
    for d in range(n_teams):
        set.append(default)
    return set

def splitting (inter, races, n_all):
    info = initialise(n_races, [])
    l = 0
    for race in races:
        split = []
        for row in range(n_all):
            split.append([inter[row]['Names'], inter[row]['Cost'], inter[row][race]])
        info[l] = split
        l += 1
        
    return info

def adding (info, rs, col):
    sub = 0
    for r in rs:
        sub += info[r][col]
        
    return sub

def new_rs (rs, s, loc):
    rs_sub = []
    for r in rs:
        rs_sub.append(r)
    for sub in range(len(s)):
        rs_sub[loc[sub]] = s[sub]
    rs_new = sorted(rs_sub)
    return rs_new

def cost_checker (comb, cost):
    if comb > cost:
        check = False
    else:
        check = True
        
    return check

def team (info, rs):
    sub = []
    for r in rs:
        sub.append(info[r][0])
        
    return sub

def complete_checker(matrix, complete, loops, n_races, n_max):        
    for race in range(n_races):
        if loops[race] == 0:
            complete[race] = True
        else:
            for n in range(loops[race]):
                if matrix[race][loops[race]-n-1] == n_max-n-1:
                    complete[race] = True
                else:
                    complete[race] = False
                    break
    
    return complete

def finished_checker(complete, n_races):
    counter = 0
    for n in range(n_races):
        if complete[n] == True:
            counter += 1
        else:
            break
            
    if counter == n_races:
        finished = True
    else:
        finished = False
    
    return finished

def checker (rs, s, loops):
    unique = True
    for race in range(1,n_races):
        for rider in range(n_riders):
            for sub in range(loops[race]):
                if s[race][sub] == rs[race-1][rider]:
                    unique = False
                    break
    
    return unique

def setup (loops, n_races):
    list = []
    
    for race in range(n_races):
        test = []
        if loops[race] != 0:
            for n in range(loops[race]):
                test.append(n)
        list.append(test)
            
    return list

def iterate (matrix, loops, r):
    matrix[r] = matrix[r] + 1
    for n in range(r+1,loops):
        matrix[n] = matrix[n-1] + 1
    
    return matrix

def loops_iterate (loops, n_races, loop_index):
    loops[loop_index] += 1
    if loop_index != n_races-1:
        for n in range(loop_index+1,n_races):
            loops[n] = 0
            
    return loops

def loops_complete_checker (loops, loops_complete, n_riders, n_races, loop_index, n_subs):
    if loops[loop_index] == n_riders:
        loops_complete[loop_index] = True
        
    if sum(loops) == n_subs:
        loops_complete[loop_index] = True
        for race in range(loop_index+1,n_races):
            loops_complete[race] = True
    else:
        loops_complete[loop_index] = False
        for race in range(loop_index+1,n_races):
            loops_complete[race] = False
            
    return loops_complete

def race_determine (complete, n_races):
    iter = 0
    
    for n in range(n_races):
        if complete[n_races-n-1] == True:
            iter += 1
        else:
            race_index = n_races-n-1
            break
            
    return race_index

def index(matrix, loops, n_max):
    for n in range(loops):
        if matrix[loops-n-1] != n_max-n-1:
            r = loops-n-1
            break
            
    return r

def no_repeat (rs, n_riders):
    repeat = False
    for m in range(n_riders-1):
        for n in range(m+1,n_riders):
            if rs[m] == rs[n]:
                repeat = True
                break
    
    return repeat

def reset (riders, loops, race_index, n_races):
    for m in range(race_index+1, n_races):
        new = []
        if loops[m] != 0:
            for n in range(loops[m]):
                new.append(n)
        riders[m] = new
    
    return riders

if gender == 'W':
    races = ['Race1', 'Race2']
if gender == 'M':
    races = ['Race1', 'Race2', 'Race3']
n_races = len(races)

in_file = open(str(race_name) + '_' + str(gender) + '.txt', 'r')
inter = []
l = 0

data = csv.DictReader(in_file)
for row in data:
    inter.append(row)
    inter[l]['Cost'] = int(inter[l]['Cost'])
    for race in races:
        inter[l][race] = int(inter[l][race])
    inter[l]['Total'] = int(inter[l]['Total'])
    l += 1
in_file.close()

n_all = len(inter)

info = splitting(inter, races, n_all)

rs = initialise(n_races, [])
comb_scores = initialise(n_races, 0)
comb_costs = initialise(n_races, 0)
squad_teams = initialise(n_races, [])
squad_scores = initialise(n_races, 0)
squad_costs = initialise(n_races, 0)
squad_total = 0

for r1 in range(n_all-5):
    print(r1)
    for r2 in range(r1+1, n_all-4):
        for r3 in range(r2+1, n_all-3):
            for r4 in range(r3+1, n_all-2):
                for r5 in range(r4+1, n_all-1):
                    for r6 in range(r5+1, n_all):
                        rs[0] = [r1, r2, r3, r4, r5, r6]
                        comb_costs[0] = adding(info[0], rs[0], 1)
                        if comb_costs[0] <= max_cost:
                            for race in range(1,n_races):
                                rs[race] = rs[0]
                            comb_scores[0] = adding(info[0], rs[0], 2)
                            loops = initialise(n_races, 0)
                            loops_complete = initialise(n_races, False)
                            loops_complete[0] = True
                            if n_subs != 0:
                                for race in range(1,n_races):
                                    loops_complete[race] = False
                            else:
                                for race in range(1,n_races):
                                    loops_complete[race] = True
                            loops_finished = False
                            while loops_finished == False:
                                s = setup(loops, n_races)
                                s_complete = initialise(n_races, False)
                                s_complete[0] = True
                                s_complete = complete_checker(s, s_complete, loops, n_races, n_all)
                                s_finished = False
                                unique = checker(rs, s, loops)
                                if unique == True:
                                    while s_finished == False:
                                        riders = setup(loops, n_races)
                                        riders_complete = initialise(n_races, False)
                                        riders_complete[0] = True
                                        riders_complete = complete_checker(riders, riders_complete, loops, n_races, n_riders)
                                        riders_finished = False
                                        while riders_finished == False:
                                            comb_total = 0
                                            for race in range(1,n_races):
                                                rs[race] = new_rs(rs[race-1], s[race], riders[race])
                                                repeat = no_repeat(rs[race], n_riders)
                                                if repeat == False:
                                                    comb_costs[race] = adding(info[race], rs[race], 1)
                                                    cost_check = cost_checker(comb_costs[race], max_cost)
                                                    if cost_check == True:
                                                        comb_scores[race] = adding(info[race], rs[race], 2)
                                                        comb_total += comb_scores[race]
                                                else:
                                                    break
                                            comb_total += comb_scores[0]
                                            if comb_total > squad_total:
                                                for race in range(n_races):
                                                    squad_teams[race] = team(info[race], rs[race])
                                                    squad_scores[race] = comb_scores[race]
                                                    squad_costs[race] = comb_costs[race]
                                                squad_total = comb_total
                                            riders_finished = finished_checker(riders_complete, n_races)
                                            if riders_finished == False:
                                                race_index = race_determine(riders_complete, n_races)
                                                r_riders = index(riders[race_index], loops[race_index], n_riders)
                                                riders[race_index] = iterate(riders[race_index], loops[race_index], r_riders)
                                                riders = reset(riders, loops, race_index, n_races)
                                                riders_complete = complete_checker(riders, riders_complete, loops, n_races, n_riders)
                                        s_finished = finished_checker(s_complete, n_races)
                                        if s_finished == False:
                                            race_index = race_determine(s_complete, n_races)
                                            r_s = index(s[race_index], loops[race_index], n_all)
                                            s[race_index] = iterate(s[race_index], loops[race_index], r_s)
                                            s = reset(s, loops, race_index, n_races)
                                            s_complete = complete_checker(s, s_complete, loops, n_races, n_all)
                                loops_finished = finished_checker(loops_complete, n_races)
                                if loops_finished == False:
                                    loop_index = race_determine(loops_complete, n_races)
                                    loops = loops_iterate(loops, n_races, loop_index)
                                    loops_complete = loops_complete_checker(loops, loops_complete, n_riders, n_races, loop_index, n_subs)
    
print('Evaluation of all combinations complete.')

out_file = open(str(race_name) + '_' + str(gender) + '_US.txt', 'w')

out_file.write('The Ultimate Squad scored ' + str(squad_total) + ' points.' + '\n' + '\n')
for race in range(n_races):
    out_file.write('The team for ' + str(races[race]) + ' was:' + '\n')
    for rider in range(n_riders):
        out_file.write(str(squad_teams[race][rider]) + '\n')
    out_file.write('Scoring ' + str(squad_scores[race]) + ' points.' + '\n')
    out_file.write('Costing ' + str(squad_costs[race]) + ' credits.' + '\n' + '\n')

out_file.close()