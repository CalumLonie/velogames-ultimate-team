# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 16:33:45 2021

@author: Calum
"""

def initialise (n_teams, default):
    set = []
    for d in range(n_teams):
        set.append(default)
    return set

def splitting (inter, races, n_all, n_races):
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

def setup (loops, n_races):
    list = []
    
    for race in range(n_races):
        test = []
        if loops[race] != 0:
            for n in range(loops[race]):
                test.append(n)
        list.append(test)
            
    return list

def iscomplete(matrix, complete, loops, n_max, n_races):        
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

def isnew (matrix, subs, loc, scope):
    new = True
    for indiv in range(scope):
        if subs[indiv] in matrix:
            new = False
            break
            
    return new

def new_rs (matrix, subs, loc, noc, scope, j):
    for indiv in range(scope[j]):
        if loc[j][indiv] in noc[j]:
            value = loc[j][indiv]
            noc[j].remove(value)
            
    for indiv in range(scope[j]):
        matrix[j][loc[j][indiv]] = subs[j][indiv]
    for indiv in range(len(noc[j])):
        matrix[j][noc[j][indiv]] = matrix[j-1][noc[j][indiv]]
    matrix[j] = sorted(matrix[j])
    
    return matrix[j]

def cost_checker (comb, cost):
    if comb > cost:
        check = False
    else:
        check = True
        
    return check

def team (info, rs, col):
    sub = []
    for r in rs:
        sub.append(info[r][col])
        
    return sub

def isfinished (complete, n_races):
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

def race_determine (complete, n_races):
    
    for n in range(n_races):
        if complete[n_races-n-1] == False:
            race_index = n_races-n-1
            break
            
    return race_index

def index(matrix, loops, n_max):
    for n in range(loops):
        if matrix[loops-n-1] != n_max-n-1:
            r = loops-n-1
            break
            
    return r

def iterate (matrix, loops, r):
    matrix[r] += 1
    for n in range(r+1,loops):
        matrix[n] = matrix[n-1] + 1
    
    return matrix

def reset (riders, loops, race_index, n_races):
    for m in range(race_index+1, n_races):
        new = []
        if loops[m] != 0:
            for n in range(loops[m]):
                new.append(n)
        riders[m] = new
    
    return riders

def loops_iterate (loops, loop_index, n_races):
    loops[loop_index] += 1
    for n in range(loop_index+1,n_races):
        loops[n] = 0
            
    return loops

def loops_iscomplete (loops, loops_complete, loop_index, n_races, n_riders, n_subs):
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