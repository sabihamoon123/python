# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:   
#     print(fruit)
#     print(fruit + "Pie")
# print(fruits)

print("Give the heights = ")
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height += height
print(f"Total height {total_height}")


number_of_students = 0 
for student in student_heights:
    number_of_students += 1
print(f"Number of students {number_of_students}")

averge_height = round(total_height / number_of_students)
print(f"Average height = {averge_height}")