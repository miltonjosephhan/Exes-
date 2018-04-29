# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 19:33:50 2018

@author: Han
"""

import random

lowercase_Letters = 'abcdefghijklmnopqrstuvwxyz'
capitalized_Letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Both_Letters = lowercase_Letters + capitalized_Letters
BothLettersAndNumbers = Both_Letters + '0123456789'

difficulty = input('How hard do you want your password to be? (Easy/Medium/Hard): ' )
passwordlength = int(input('How many characters do you want your password to be?: '))

password = ''

for i in range(passwordlength):
    if (difficulty == 'Easy'):
        password = password + lowercase_Letters[random.randint(0, len(lowercase_Letters)-1)]
    elif (difficulty == 'Medium'):
        password = password + Both_Letters[random.randint(0, len(Both_Letters)-1)]
    elif (difficulty == 'Hard'):
        password = password + BothLettersAndNumbers[random.randint(0, len(BothLettersAndNumbers)-1)]
        
print('your password: ' + password)