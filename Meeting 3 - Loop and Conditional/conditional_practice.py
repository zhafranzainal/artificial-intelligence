students_name = ['Alex', 'Bryan', 'Christ', 'Dave', 'Eva']
students_score = [95, 80, 75, 90, 65]
students_grade = []

for score in students_score:
    if score >= 90:
        students_grade.append('A')
    elif score >= 70:
        students_grade.append('B')
    else:
        students_grade.append('C')

print()
print(students_grade)

students_grade = ['A' if score >= 90 else
                  'B' if score >= 70 else 'C'
                  for score in students_score]

print()
print(students_grade)
