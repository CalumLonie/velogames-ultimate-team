# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 14:07:42 2021

@author: Calum
"""
import csv


def data_read (path, race_type, year, race_name, suffix):
    in_file = open(path + race_type + '/' +  year + '/' + race_name + suffix, 'r')
    info = []
    l = 0
    
    data = csv.DictReader(in_file)
    for row in data:
        info.append(row)
        info[l]['Cost'] = int(info[l]['Cost'])
        info[l]['Points'] = int(info[l]['Points'])
        l += 1
        
    in_file.close()
    
    return info

def filtering (info, n_iter, n_riders, ratio):
    filtered_names = []
    filtered_cost = []
    filtered_points = []
    l = 0
    cost = 0
    counter = 0
    
    for l in range(n_iter):
        if info[l]['Cost'] != cost:
            cost = info[l]['Cost']
            counter = 1
        else:
            counter += 1
    
        if counter <= n_riders:
            if info[l]['Points'] / info[l]['Cost'] >= ratio:
                filtered_names.append(info[l]['Names'])
                filtered_cost.append(info[l]['Cost'])
                filtered_points.append(info[l]['Points'])
                
    return filtered_names, filtered_cost, filtered_points

def filtering_GT (info, n_iter, n_max):
    filtered_names = []
    filtered_cost = []
    filtered_points = []
    cost = 0
    counter = 0
    
    for l in range(n_iter):
        if info[l]['Cost'] != cost:
            cost = info[l]['Cost']
            counter = 1
        else:
            counter += 1
            
        if counter <= n_max:
            # Insert ratio filtering here
            filtered_names.append(info[l]['Names'])
            filtered_cost.append(info[l]['Cost'])
            filtered_points.append(info[l]['Points'])
            
    n_filtered = len(filtered_names)
    
    return filtered_names, filtered_cost, filtered_points, n_filtered

def filter_out (path, race_type, year, race_name, suffix, filtered_names, filtered_cost, filtered_points, n_filtered):
    out_file = open(path + race_type + '/' + year + '/' + race_name + suffix, 'w')
    out_file.write('Names,Cost,Points' + '\n')
    for r in range(n_filtered):
        out_file.write(filtered_names[r] + ',' + str(filtered_cost[r]) + ',' + str(filtered_points[r]) + '\n')
    out_file.close()
    
    return

def initialise (n_iter, default):
    set = []
    for d in range(n_iter):
        set.append(default)
    return set

def adding (info, rs, col):
    sub = 0
    for r in rs:
        sub += info[r][col]
        
    return sub

def team (info, rs, col):
    sub = []
    for r in rs:
        sub.append(info[r][col])
        
    return sub

def rs_iterate(matrix, complete, n_iter):
    for iter in range(n_iter):
        if complete[n_iter - iter - 1] == False:
            matrix[n_iter - iter - 1] += 1
            index = n_iter - iter - 1
            if index == 0:
                print(matrix[0] - 1)
            break
        
    for iter in range(1, n_iter - index):
        matrix[index + iter] = matrix[index + iter - 1] + 1
    
    return matrix

def complete_checker(matrix, complete, n_iter, n_max):
    for iter in range(n_iter):
        if matrix[n_iter - iter - 1] == n_max - iter - 1:
            complete[n_iter - iter - 1] = True
        else:
            complete[n_iter - iter - 1] = False
            
    return complete

def finished_checker (complete, n_iter):
    counter = 0
    for iter in range(n_iter):
        if complete[iter] == True:
            counter += 1
        else:
            break
            
    if counter == n_iter:
        finished = True
    else:
        finished = False
    
    return finished