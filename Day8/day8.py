# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 06:32:46 2023

@author: TJaeckel
"""
import re
from math import lcm

mapdata = open(r"C:\Users\tonyj\OneDrive\Documents\Python Scripts\Advent 2023\Day8\input.txt").readlines()

class Node:
    name = ""
    left = ""
    right = ""
    
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right
        
directions = [c for c in mapdata[0].strip()]
steps = {}
for path in mapdata:
    
    if "=" in path:
        splitpath = path.split("=")
        name = splitpath[0].strip()
        nextsteps = re.findall("\w{3}", splitpath[1])
        steps[name] = Node(name, nextsteps[0], nextsteps[1])

starts = list(filter(lambda x: re.findall("\w\wA", x), steps.keys()))
ends = list(filter(lambda x: re.findall("\w\wZ", x), steps.keys()))

currentnode = "AAA"
values = []
for currentnode in starts:
    c = 1
    Found = False
    while not Found:
        #c -= 1
        for x in directions:
           
           if x == "L":
               currentnode = steps[currentnode].left
           elif x == "R":
               currentnode = steps[currentnode].right
           if currentnode in ends:
               print(c + 1)
               Found = True
               break
           c += 1
    values.append(c)
           
print(lcm(*values))    