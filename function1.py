# def greet():
#     print("Hello!")
#     print("How are you?")
#     print("Where is your home district?")

# greet()

# def greet_with_name(name):
#     print(f"Hello! {name}")
#     print(f"How are you? {name}")

# greet_with_name(name="Moon")

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"I am from {location}")

# greet_with(name="Moon", location="Dhaka")

import math


def paint_calc(height, width, cover):
    no_cans = (height * width) /cover
    round_up_number = math.ceil(no_cans)
    print(f"The number of cans = {round_up_number}")


test_h = int(input())
test_w = int(input())
coverage = 5
paint_calc(height=test_h, width=test_w ,cover=coverage)