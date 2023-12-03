# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import re

path = r"C:\Users\tonyj\OneDrive\Documents\Python Scripts\Advent 2023\Day 2\day2.txt"



games = open(path).readlines()
total = 0
for game in games:
    max_colors = {"red":0, "green":0, "blue":0}
    gamePass = True
    gamePlayed = game.split(":")
    roundList = gamePlayed[1].split(";")
    
    for gameRound in roundList:

        hands = gameRound.split(",")
        for hand in hands:

            pull = hand.strip().split(" ")
            if int(pull[0].strip()) > max_colors[pull[1].strip()]:
                max_colors[pull[1].strip()] = int(pull[0].strip())
    values = list(max_colors.values())
    total += (values[0] * values[1] * values[2])
print(total)
        
