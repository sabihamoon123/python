# import random

# random_integer = random.randint(1, 10)

# print(random_integer)

# random_float = random.random() * 5
# print(random_float)

# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")

# random_side = random.randint(0, 1)
# if random_side == 1:
#     print("Head")
# else:
#     print("Tail")
names_string = str(input())
person_who_will_pay = int(input())

names = names_string.split(" , ")
import random
num_items = len(names)

random_choice = random.randint(0, num_items - 1)
print (person_who_will_pay + " is going to buy the meal today!")
