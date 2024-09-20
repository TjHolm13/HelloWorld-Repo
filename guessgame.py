"""
Tatem Holm
9/17/2024
This program will play a game with the user
"""

import random
computer_num = random.randint(0,100)
keep_playing = True

while keep_playing:
	user_guess = int(input('Please guess a number between 1 and 100: '))
	if user_guess == computer_num:
		print('Congrats You Win')
		keep_playing = False
	elif user_guess < computer_num:
		print('Your number is too small')
	elif user_guess > computer_num:
		print('Your number is too large')
	else:
		print('error')
