"""
Tatem Holm
9/6/2024
This program will convert human years into dog years
"""
human_age = float(input('Enter your age: '))
dog_age = human_age * 7
dog_years = int(dog_age)
dog_months = int((dog_age % 1) * 12)
dog_days =  int((((dog_age % 1) *12) % 1) * 30)

print(f' Your age in dog years is , {dog_years:.1f}, years, {dog_months:.1f}, months, {dog_days:.1f}, days')

cat_age = human_age / 9
cat_years = int(cat_age)
cat_months = int((cat_age % 1) * 12)
cat_days = int((((cat_age % 1) *12) % 1) * 30)
print(f' Your age in cat years is , {cat_years:.1f}, years, {cat_months:.1f}, months, {cat_days:.1f}, days')

horse_age = 3 * (((human_age ** 2 - 47) / 7) + 12)
horse_years = int(horse_age)
horse_months = int((horse_age % 1) * 12)
horse_days = int((((horse_age % 1) *12) % 1) * 30)

print(f' Your age in horse years is , {horse_years:.1f}, years, {horse_months:.1f}, months, {horse_days:.1f}, days')

