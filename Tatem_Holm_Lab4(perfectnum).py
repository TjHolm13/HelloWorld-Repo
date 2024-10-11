'''
Tatem Holm
9/20/2024
This program will output the amount of deficient, perfect, and abundant numbers
between 1 and some upper bound specidied by the user
'''
def classify_number(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    sum_divisors = sum(divisors)
    
    if sum_divisors < n:
        return 'deficient'
    elif sum_divisors == n:
        return 'perfect'
    else:
        return 'abundant'

def count_classifications(upper_bound):
    counts = {'deficient': 0, 'perfect': 0, 'abundant': 0}
    
    for i in range(1, upper_bound + 1):
        classification = classify_number(i)
        counts[classification] += 1
    
    return counts

upper_bound = int(input("Enter an upper bound for a check: "))
counts = count_classifications(upper_bound)

print(f"Between 1 and {upper_bound} there are")
print(f"{counts['deficient']} deficient numbers")
print(f"{counts['perfect']} perfect numbers")
print(f"{counts['abundant']} abundant numbers")
