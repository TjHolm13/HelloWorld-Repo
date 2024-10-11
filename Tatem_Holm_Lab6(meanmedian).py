"""
Tatem Holm
10/4/2024
Lab 6 - Lists
"""


# Arithmetic with corresponding elements of mutiple lists.
	#Test1 - correct answer = 8
#list1, list2, list3 = [1,2,3], [4,5,6], [7,8,9]
	#Test 2 - correct answer = 21
#list1, list2, list3 = [5,-2,4], [3,12,9], [8,4,-6]
	#Test 3 - correct answer = 0
#list1, list2, list3 = [], [], []
	#Test 4 - correct answer = -7
#list1, list2, list3 = [7,3,5,7,1], [2,2,3,-3,4], [5,6,5,4,5]
	#Test 5 - correct answer = All lists are required to be the same length
#list1, list2, list3 = [4,4], [3,2], [8,9,1]
	#Test 6 - correct answer = 74.142
#list1, list2, list3 = [6.3,8.4,9.2], [-1.2,7.6,3.2], [4.1,-2.1,9.6]


"""
# Problem 1
### My Code ###
variable = 0
if len(list1) == len(list2) and len(list1) == len(list3):
	for i in range(len(list1)):
		answer = list1[i] * list2[i] - list3[i]
		variable += answer
	print(variable)
else:
	print('All lists are required to be the same length')
"""


"""
# Problem 2
### My Code ###
new_list = []
if len(list1) == len(list2) and len(list1) == len(list3):
	for i in range(len(list1)):
		new_num = list1[i] * list2[i] - list3[i]
		new_list.append(new_num)
	print(new_list)
else:
	print('All lists are required to be the same length')
"""


	#Test1 - Mean = 3, Median = 3
data_set_1 = [3,2,1,4,5]
	# Test2 - Mean = 6.1146, Median = 6
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
	#Test3 - 
data_set_3 = []


"""
# Problem 3
### My Code ###
data = data_set_1
if len(data) >= 1:
	data.sort()
	variable = len(data)
	data_sum = sum(data)
	mean = data_sum / variable
	
	if variable % 2 == 0:
		median1 = data[variable // 2]
		median2 = data[variable // 2 - 1]
		true_median = (median1 + median2) / 2
	else:
		true_median = data[variable // 2]
	print(f"Mean:{mean:.4f} Median:{true_median}")
else:
	print('Mean: 0 Median: 0')
"""
