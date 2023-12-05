# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 07:23:22 2023

@author: TJaeckel
"""

import re
import pandas as pd

maps = {"seed-to-soil map:": [], "soil-to-fertilizer map:": [], "fertilizer-to-water map:": [], 
        "water-to-light map:": [], "light-to-temperature map:": [], "temperature-to-humidity map:": [], "humidity-to-location map:": []}

almanac = open(r"C:\Users\tonyj\OneDrive\Documents\Python Scripts\Advent 2023\Day 5\input.txt").read()

allseeds = [1514493331, 295250933, 3793791524, 105394212, 828589016, 654882197, 658370118,
            49359719, 4055197159, 59237418, 314462259, 268880047, 2249227634, 74967914, 
            2370414906, 38444198, 3291001718, 85800943, 2102534948, 5923540]
#allseeds = [5923540]
allvalues = re.findall("(\w+-\w+-\w+\smap:\n)?(\d+\s\d+\s\d+\n)", almanac)
del allvalues[0]
currentMap= ""

for value in allvalues:
    #print(value[0])
    if value[0].strip() in maps.keys():
        currentMap = value[0].strip()
    maps[currentMap].append(value[1].split(" "))

minseedlocation = 9999999999999999999999
seedlocations = {}
for x in range (0, 18, 2):
    print(x)
    low = int(allseeds[x])
    high = int(allseeds[x+1])
    for seed in range(low, low + high):
        origseed = seed
        seedvalues = {}
        for key in maps.keys():
            seedvalues[key] = seed
            for value in maps[key]:
                if int(seed) == int(value[1]):
                    seedvalues[key] = int(value[0])
                    seed = seedvalues[key]
                    break
                elif int(value[1]) < int(seed) <= int(value[1]) + int(value[2]):
                    diff = int(value[1]) - int(value[0])
                    seedvalues[key] = seed - diff
                    seed = seedvalues[key]
                    break
        
        if seedvalues["humidity-to-location map:"] < minseedlocation:
            minseedlocation = seedvalues["humidity-to-location map:"]




