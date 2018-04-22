# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 09:44:57 2018

@author: Han
"""


#print('What is your name?')
#name = input()

#print('ok, ' + name + ' what is your age?')
#age = int(input())

#ducks = 100 - age 

#print('You are ' + str(age) + ' years old.') 
#print(' Interesting, you will be 100 in the year: ' + str(2018 + ducks))

player1 = input('What is your name?')
player2 = input('And what about you?')

print('Well, you guys are going to play a game of rock, paper, scissors'  )

p1_answer = input('What do you choose ' + player1 + '?')

p2_answer = input('Okay, and what about you ' + player2 + '?')

if p1_answer == p2_answer:
    print('Sorry its a tie, try again')
    
if p2_answer == 'scissors':
    if p1_answer == 'rock':
        print('Rock beats scissors ' + player1 + ' wins!')
        
if p1_answer == 'paper':
    if p2_answer == 'rock': 
        print('Paper beats rock ' + player1 + ' wins!')
        
if p1_answer == 'scissors':
    if p2_answer == 'paper':
        print('Scissors beats paper ' + player1 + ' wins!')
        
if p2_answer == 'rock':
    if p1_answer == 'scissors':
        print('Rock beats scissors ' + player2 + ' wins!')
        
if p2_answer == 'paper':
    if p1_answer == 'rock':
        print('Paper beats rock ' + player2 + ' wins!')
        
if p2_answer == 'scissors':
    if p1_answer == 'paper':
        print('Scissors beats paper ' + player2 + ' wins!')
    
       





        
        
    


