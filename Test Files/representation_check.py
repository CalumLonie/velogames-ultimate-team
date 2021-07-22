# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 23:48:12 2020

@author: Calum
"""

import csv

# Test special characters
input_file = open('Test_Sprinter.txt', 'r')
info = []
l = 0

data = csv.DictReader(input_file)
for row in data:
    info.append(row)
    info[l]['Cost'] = int(info[l]['Cost'])
    info[l]['Points'] = int(info[l]['Points'])
    l += 1
input_file.close()

rider = info[3]['Name']
print(rider)