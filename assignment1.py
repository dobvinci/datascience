#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 13:42:39 2019
#i can read your mind game
@author: dobvinci
"""

def letsGo(start,end):
        count=0
        gameison = True
        while gameison:
            count+=1
            ans = (start + end)//2
            print("Are you thinking about " + str(ans) + "? ")

            userinput = input("Reply with 'l' if number is low,\n'h' if high and \n'y' for right answer.\nResponse:")

            if userinput == "h":
                end = ans
            elif userinput == "l":
                start = ans
            elif userinput == "y":
                print("Yipee!!\n I told you i could guess : " + str(ans)+" in not more than "+str(count)+ " times")
                break
            else:
                print(":-( Iko shida Boss,Weka namba....")
	
        
def main():
        print("I can read your mind,\nguess any number between 0 and 1000,000")
        end= int(input("What is your limit?:"))
        if end<0 or end>1000000:
             print("Your upper limit must be less than 1M and not less than 0!!,Bye")
        else:
                 
            start=0
       # end=100
            letsGo(start,end)
      
main()