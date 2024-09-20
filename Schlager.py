'''
Tatem Holm
9/17/2024
This program will print words backwords
'''
keep_going = True
while keep_going:
    word = str(input())
    if word == 'Done':
        keep_going = False
    elif word == 'done':
        keep_going = False
    elif word == 'd':
        keep_going = False
    elif word == 'D':
        keep_going = False
    else:
        print(word[-1::-1])
