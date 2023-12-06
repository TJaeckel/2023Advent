import re
import pandas as pd


racedata = open(r"C:\Users\tonyj\OneDrive\Documents\Python Scripts\Advent 2023\Day 6\input.txt").readlines()

racetime = racedata[0].split(":")[1]
racetime = int(racetime.replace(" ", ""))

racedistance = racedata[1].split(":")[1]
racedistance = int(racedistance.replace(" ", ""))

df = pd.DataFrame({'charge': range(0, racetime) , "winningdistance":racedistance})
df["mysdistance"] = df["charge"] * (racetime - df["charge"])

finaldf = df[df["mysdistance"] > df["winningdistance"]]

print(finaldf.count())
