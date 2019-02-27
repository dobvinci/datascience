#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 19:36:43 2019
Pandas 
@author: dobvinci
"""

import pandas as pow #what is this called i.e. 'import abcdef as g
import numpy as np 

#The Scores
# group 1
sell = {"presentation" : [3,4,3],
"team_work" : [3,5,4],
"innovativeness" : [7,8,5]}
#group 2
tumeiva = {"presentation" : [2,1,2],
"team_work" : [2,0,3],
"innovativeness" : [5,4,6]}
#group 3
three = {"presentation" : [3,3,4],
"team_work" : [5,4,5],
"innovativeness" : [10,5,3]}
#group 4
wtot ={"presentation" : [4,3,5],
"team_work" : [4,5,5],
"innovativeness" : [5,7,6]}
keys_score = ["presentation","team_work","innovativeness"]
scores = pow.DataFrame({'sell': sell,'tumeiva' : tumeiva,"three" : three,'wtot':wtot})
print(scores)

#question 1

print("***********group with highest presentation score**************\n\n")
max_presentation=max({"sell":np.sum(scores.sell.presentation),"tumeiva":np.sum(scores.tumeiva.presentation),"three":np.sum(scores.three.presentation),"wtot":np.sum(scores.wtot.presentation)})
print("group with highest presentation score is {}".format(max_presentation),"\n\n")

print("*******************Alternatively....simper************************\n\n")

maximum_presentation=max(scores.loc[['presentation'],['sell','tumeiva','three','wtot']])


print("group with highest presentation score is {}".format(max_presentation),"\n\n")

#question 2

print("***********group with highest overall score**************\n\n")

#sum_highest_score=np.max([scores.sell.sum(),scores.tumeiva.sum(),scores.three.sum(),scores.wtot.sum()])
highest_overall=max({"sell":np.sum(np.array(scores.sell.sum())),"tumeiva":np.sum(np.array(scores.tumeiva.sum())),"three":np.sum(np.array(scores.three.sum())),"wtot":np.sum(np.array(scores.wtot.sum()))})
print("group with highest overall score is {}".format(highest_overall),"\n\n")
idx = pow.MultiIndex
print("ines",idx.max)
#question 3

print("***********group function to get score**************\n\n")


def scoreFunct(title,dt):
    if title == "":
        return max({"sell":np.mean(np.sum(dt.sell)),"tumeiva":np.mean(np.sum(dt.tumeiva)),"three":np.mean(np.sum(dt.three)),"wtot":np.mean(np.sum(dt.wtot))})
    else:
        try:
            return max(scores.loc[[title],['sell','tumeiva','three','wtot']])
        except:
            return "error"
   
    
title="team_work"
print("the group {}  has highest average  is {}".format(title,scoreFunct(title,scores)))

    