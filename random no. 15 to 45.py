import random
random_numbers = set(random.randint(15, 45) for _ in
range(10))
count_less_than_30 = sum(1 for num in random_numbers if
num < 30)
print("Generated numbers:", random_numbers)
print("Number of elements less than 30:", 
count_less_than_30)
# Delete all numbers greater than 35
random_numbers = {num for num in random_numbers if num
<= 35}
print("Set after deleting numbers greater than 35:", 
random_numbers