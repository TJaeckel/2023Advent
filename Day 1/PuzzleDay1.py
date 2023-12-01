# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 07:23:15 2023
"""

import pandas as pd
import re

numbers = {"zero":0, "one":1, "two":2,"three":3 ,"four":4 ,"five":5 ,"six":6 ,"seven":7 ,"eight":8 ,"nine":9, "eightwo": 82, "oneight": 18, "twone": 21}

def convert(x):
    returnlist = []
    for digit in x:
        if digit in numbers.keys():
            digit = numbers[digit]
        if int(digit) > 9:
            returnlist.extend(int(d) for d in str(digit))
        else:
            returnlist.append(digit)
    return returnlist

def getFirstandLastNumber(text):
    regex = r"(?:twone)|(?:oneight)|(?:eightwo)|(?:one)|(?:two)|(?:three)|(?:four)|(?:five)|(?:six)|(?:seven)|(?:eight)|(?:nine)|(?:zero)|\d"
    parsed = re.findall(regex, text)

    parsed = convert(parsed)
    returning = int("{}{}".format(parsed[0], parsed[-1]))
    return returning

file = open(r"File Location").readlines()

df = pd.DataFrame(file)

df["Values"] = df[0].apply(lambda x: getFirstandLastNumber(x))
print(df["Values"].sum())
