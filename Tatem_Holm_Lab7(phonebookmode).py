"""
Tatem Holm
10/11/2024
Lab 6 - Dictionaries
"""
"""
# Problem 1
# Create a phone book.
print("When entering a name and number, please enter names with underscores.\n" +
      "For example: Matt_Priem, 507-389-1438. When done, type 'quit'\n")
      
###MyCode###
phone_book = {}
keep_asking = True
while keep_asking == True:
	user_input = input('Name and Number: ')
	if user_input == 'quit':
		print(f'Your phone book consist of {phone_book}')
		keep_asking = False
	else:
		user_name, user_number = user_input.split()
		phone_book[user_name] = user_number
"""

#Problem 2
	#Test1 - Mode = 2
data_set_1 = [3,3,2,2,2,2,4,4,4,14,14]
	# Test2 - Mode = 5
data_set_2 = [
		10, 8, 5, 3, 6, 8, 8, 6, 7, 3, 6, 4, 6, 10, 6, 6, 9, 6, 10, 8, 
		4, 6, 5, 7, 4, 5, 2, 4, 2, 6, 10, 3, 2, 5, 5, 6, 4, 3, 2, 9, 3, 
		5, 9, 9, 9, 6, 7, 5, 5, 6, 5, 8, 10, 4, 9, 3, 3, 10, 7, 8, 2, 6, 
		4, 7, 9, 9, 8, 8, 3, 9, 7, 4, 3, 9, 8, 4, 9, 3, 7, 2, 10, 10, 8, 
		6, 4, 7, 10, 8, 4, 4, 5, 4, 9, 3, 8, 2, 5, 8, 10, 5, 10, 7, 2, 
		3, 3, 5, 3, 4, 8, 10, 9, 7, 5, 9, 5, 5, 2, 6, 10, 9, 4, 2, 9, 
		10, 7, 10, 8, 4, 10, 6, 10, 10, 4, 2, 6, 2, 3, 5, 8, 5, 10, 8, 
		7, 5, 10, 7, 5, 9, 5, 5, 10, 5, 7, 2, 3, 2, 2
	]
	#Test3 - This data set is multimodal.  The modes are 2 and 4.
data_set_3 = [1,2,2,2,3,3,4,4,4,5]


###MyCode###
data = data_set_3
numbers = {}
for number in data:
	if number in numbers:
		numbers[number] += 1
	else:
		numbers[number] = 1
get_mode = max(numbers.values())
mode = []
for key,value in numbers.items():
	if value == get_mode:
		mode.append(key)
print(f"Mode: {mode}")



