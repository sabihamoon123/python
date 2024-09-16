students_score = {
    "Harry" : 81,
    "Ron" : 78,
    "Harmione" : 99,
    "Draco" : 74,
    "Neville" : 62,
}

student_grades = {}
for students in students_score:
    score = students_score[students]
    if score > 90:
        student_grades[students] = "Outstanding"
    elif score > 80:
        student_grades[students] = "Exceeds expectation"
    elif score > 70:
        student_grades[students] = "Acceptable"
    else:
        student_grades[students] = "Fall"

print(student_grades)