# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 14:23:14 2022

@author: shrih
"""
score=0
def check(guess,answer):
    global score
    if guess.lower()==answer.lower():
        score+=1
        print("score ",score)
        print("correct")
    else:
        score=0
        print("Incorrect")
        print("score ",score)
print("guess the country")
guess1=input("which country has the highest population? ")
check(guess1,'China')

guess2=input("What is the capital of Bulgaria? ")
check(guess2,'Sofia')

guess3=input("Who won the ODI world cup in 2019? ")
check(guess3,'England')

guess4=input("What is the capital of Belgium? ")
check(guess4,'Brussels')

guess5=input("What is the capital of Belarus? ")
check(guess5,'Minsk')

print("Thank you for taking this quiz")
