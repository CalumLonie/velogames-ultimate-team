# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 15:30:14 2020

@author: Calum
"""


import csv

race_name = 'Test'
n_c = 6
n_s = 6
n_tt = 6
n_all = n_c + n_s + n_tt

n_teams = 10
n_riders = 7

def initialise (n_teams, default):
    set = []
    for d in range(n_teams):
        set.append(default)
    return set

def assignment (set, comb, n_teams, index):
    n = n_teams - index - 1
    if n != 0:
        for t in range(n):
            set[n-t] = set[n-t-1]
    set[index] = comb
    return set

def checker (comb_riders, set_riders, info_w, n_teams):
    [comb_c_sort, comb_s_sort, comb_tt_sort] = sorting(comb_riders, info_w)
    
    for team in range(n_teams):
        if set_riders[team] != []:
            [set_c_sort, set_s_sort, set_tt_sort] = sorting(set_riders[team], info_w)
            unique = True
            counter = 0
            if comb_c_sort == set_c_sort:
                counter += 1
            if comb_s_sort == set_s_sort:
                counter += 1
            if comb_tt_sort == set_tt_sort:
                counter += 1
            if counter == 3:
                unique = False
                break
        else:
            unique = True
            
    return unique

def sorting (into, info_w):
    out_c = sorted([into[0], into[1]])
    out_s = sorted([into[2], into[3]])
    out_tt = sorted([into[4], into[5]])
                    
    for row in range(len(info_w)):
        if into[6] == info_w[row]['Name']:
            j = row
            break
    
    if j+1 <= n_c:
        out_c.append(into[6])
        out_c = sorted(out_c)
    elif j+1 <= n_c + n_s:
        out_s.append(into[6])
        out_s = sorted(out_s)
    else:
        out_tt.append(into[6])
        out_tt = sorted(out_tt)
        
    return out_c, out_s, out_tt

# For Climbers
climber_file = open(race_name + '_Climber' + '.txt', 'r')
info_c = []
l_c = 0

data = csv.DictReader(climber_file)
for row in data:
    info_c.append(row)
    info_c[l_c]['Cost'] = int(info_c[l_c]['Cost'])
    info_c[l_c]['Points'] = int(info_c[l_c]['Points'])
    l_c += 1
       
climber_file.close()

# For Sprinters
sprinter_file = open(race_name + '_Sprinter' + '.txt', 'r')
info_s = []
l_s = 0

data = csv.DictReader(sprinter_file)
for row in data:
    info_s.append(row)
    info_s[l_s]['Cost'] = int(info_s[l_s]['Cost'])
    info_s[l_s]['Points'] = int(info_s[l_s]['Points'])
    l_s += 1
       
sprinter_file.close()

# For TTers
tt_file = open(race_name + '_TT' + '.txt', 'r')
info_tt = []
l_tt = 0

data = csv.DictReader(tt_file)
for row in data:
    info_tt.append(row)
    info_tt[l_tt]['Cost'] = int(info_tt[l_tt]['Cost'])
    info_tt[l_tt]['Points'] = int(info_tt[l_tt]['Points'])
    l_tt += 1
       
tt_file.close()

# For Wildcard
wildcard_file = open(race_name + '_Wildcard' + '.txt', 'r')
info_w = []
l_w = 0

data = csv.DictReader(wildcard_file)
for row in data:
    info_w.append(row)
    info_w[l_w]['Cost'] = int(info_w[l_w]['Cost'])
    info_w[l_w]['Points'] = int(info_w[l_w]['Points'])
    l_w += 1
       
wildcard_file.close()

set_riders = initialise(n_teams, [])
set_scores = initialise(n_teams, 0)
set_costs = initialise(n_teams, 0)

for c1 in range(n_c-1):
    for c2 in range(c1+1,n_c):
        for s1 in range(n_s-1):
            for s2 in range(s1+1,n_s):
                for tt1 in range(n_tt-1):
                    for tt2 in range(tt1+1,n_tt):
                        for w in range(n_all):
                            if w != c1 and w != c2 and w != s1+n_c and w != s2+n_c and w != tt1+n_c+n_s and w != tt2+n_c+n_s:
                                comb_cost = info_c[c1]['Cost'] + info_c[c2]['Cost'] + info_s[s1]['Cost'] + info_s[s2]['Cost'] + info_tt[tt1]['Cost'] + info_tt[tt2]['Cost'] + info_w[w]['Cost']
                                if comb_cost <= 50:
                                    comb_riders = [info_c[c1]['Name'], info_c[c2]['Name'], info_s[s1]['Name'], info_s[s2]['Name'], info_tt[tt1]['Name'], info_tt[tt2]['Name'], info_w[w]['Name']]
                                    comb_score = info_c[c1]['Points'] + info_c[c2]['Points'] + info_s[s1]['Points'] + info_s[s2]['Points'] + info_tt[tt1]['Points'] + info_tt[tt2]['Points'] + info_w[w]['Points']
                                    unique = checker(comb_riders, set_riders, info_w, n_teams)
                                    replaced = False
                                    for index in range(n_teams):
                                        if comb_score > set_scores[index] and unique and not replaced:
                                            set_riders = assignment(set_riders, comb_riders, n_teams, index)
                                            set_scores = assignment(set_scores, comb_score, n_teams, index)
                                            set_costs = assignment(set_costs, comb_cost, n_teams, index)
                                            replaced = True
                                            
out_file = open(str(race_name) + '_Top' + str(n_teams) + '.txt', 'w')
for team in range(n_teams):
    out_file.write('Team number ' + str(team+1) + ':' + '\n')
    for rider in range(n_riders):
        out_file.write(set_riders[team][rider] + '\n')
    out_file.write('Scoring ' + str(set_scores[team]) + ' points.' + '\n')
    out_file.write('Costing ' + str(set_costs[team]) + ' credits.' + '\n')
    out_file.write('\n')
out_file.close()

UT_file = open(str(race_name) + '_UT.txt', 'w')
UT_file.write('The Ultimate Team is:' + '\n')
for rider in range(n_riders):
    UT_file.write(str(set_riders[0][rider]) + '\n')
UT_file.write('Scoring ' + str(set_scores[0]) + ' points.' + '\n')
UT_file.write('Costing ' + str(set_costs[0]) + ' credits.')
UT_file.close()
