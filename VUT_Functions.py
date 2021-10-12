# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 14:07:42 2021

@author: Calum
"""


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