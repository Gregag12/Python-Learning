student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for key in student_scores:
    if student_scores[key] >= 91:
        student_grades[key] = "Outstanding"
    elif student_scores[key] > 80 < 91:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] > 70 < 81:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_grades["Harry"])
print(student_grades["Ron"])
print(student_grades["Hermione"])
print(student_grades["Draco"])
print(student_grades["Neville"])

