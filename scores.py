# student_scores = input().split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])

# highest_score = 0 
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score 

# print(f"The highest score is = {highest_score}")

# total = 0 
# for number in range(1, 101):
#   total += number

# print(total)

target = int(input())
even_sum = 0
for number in range(2, target+1, 2):
    even_sum += number
print(even_sum)