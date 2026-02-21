import random

# a to b including a and b
val = random.randint(1,100)
print(val)

# 0 to 1, >=0 and less than 1
res = random.random()
print(res)

# float a ≤ N ≤ b (in theory) 
# but in practical You should assume the range is [1.0, 10.0)
# (includes 1.0, excludes 10.0)
res1 = random.uniform(1,10)
print(res1)


list1 = ["Alex", "Bob", "Charlie", "David", "Eve"]
# randomly select an item from the list
name = random.choice(list1)
print(name)
random_index = random.randint(0, len(list1)-1)
print(list1[random_index])