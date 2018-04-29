# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 09:44:57 2018

@author: Han
"""


player1 = input('What is your name?')
player2 = input('And what about you?')

print('Well, you guys are going to play a game of rock, paper, scissors'  )

p1_answer = input('What do you choose ' + player1 + '?')

p2_answer = input('Okay, and what about you ' + player2 + '?')

for i in range(3): 
    p1_answer = input(str(player1) + ", please choose 'rock,' 'paper,' or 'scissors.' ")
    if p1_answer == 'rock' or p1_answer == 'paper' or p1_answer == 'scissors': 
        print('Valid Input')
        break
    if p1_answer != 'rock' or p1_answer != 'paper' or p1_answer != 'scissors':
        print("You need to enter in 'rock,' 'paper,' or 'scissors.'")    
      
"""
for p1_answer in range (3):
    if p1_answer == 'rock' or 'paper' or 'scissors':
    print("Guess again with the right entry") 
       input(str(player1) + ", please choose 'rock,' 'paper,' or 'scissors' again. ")
        break
"""

for i in range (3):
    p2_answer = input(str(player2) + ", please choose 'rock,' 'paper,' or 'scissors.' ")
    if p2_answer == 'rock' or p2_answer == 'paper' or p2_answer == 'scissors': 
       print('Correct Input')
       break
    if p2_answer != 'rock' or p2_answer != 'paper' or p2_answer != 'scissors':     
       print ("Please enter in 'rock,' 'paper,' or 'scissors.'")  
       
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
        
        
      

   
else: 
       print("Invalid entry. Please choose 'rock,' 'paper,' or 'scissors' next time.")     
    
       





        
        
    


