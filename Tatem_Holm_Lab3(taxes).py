"""
Tatem Holm
9/13/2024
This program will ask for your earned income and martial status
and will calculate how much you owe in taxes for 2023
"""

income = int(input('Please enter your earned income: '))
print('Are you Married or Single?')
ms_status = input('Type m for married and s for single: ')
taxs_10 = income*.10
taxs_12 = 11000 * .10 + ((income - 11000) * .12)
taxs_22 = 11000 * .10 + (33725 * .12) + ((income - 44725) * .22)
taxm_10 = income*.10
taxm_12 = 22000 * .10 + ((income - 22000) * .12)
taxm_11 = 22000 * .10 + (67450 * .12) + ((income - 89450) * .22)

if ms_status == 's':
	if income >= 95376:
		print('You made too much money for this calculator. Hurray!')
	elif income >= 44726:
		print(f'This year you owe {taxs_22} in taxes')
	elif income >= 11001:
		print(f'This year you owe {taxs_12} in taxes')
	elif income >= 0:
		print(f'This year you owe {taxs_10} in taxes')
elif ms_status == 'm':
	if income >= 190751:
		print('You made too much money for this calculator. Hurray!')
	elif income >= 89451:
		print(f'This year you owe {taxm_22} in taxes')
	elif income >= 22001:
		print(f'This year you owe {taxm_12} in taxes')
	elif income >= 0:
		print(f'This year you owe {taxm_10} in taxes')
else:
	print('error')
