# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import re

path = r"C:\Users\tonyj\OneDrive\Documents\Python Scripts\Advent 2023\Day 2\day2.txt"

max_colors = {"red":12, "green":13, "blue":14}

games = open(path).readlines()
total = 0
for game in games:
    gamePass = True
    gamePlayed = game.split(":")

    roundList = gamePlayed[1].split(";")
    for gameRound in roundList:
        if not gamePass:
            break
        hands = gameRound.split(",")
        for hand in hands:
            if not gamePass:
                break
            pull = hand.strip().split(" ")
            if int(pull[0].strip()) > max_colors[pull[1].strip()]:
                gamePass = False
    if gamePass:
        total += int(re.findall("\d+", gamePlayed[0])[0])
print(total)
        
