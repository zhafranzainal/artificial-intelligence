students_name = ['Alex', 'Bryan', 'Christ', 'Dave', 'Eva']
students_score = [95, 80, 75, 90, 65]
students_grade = []

print()
for score in students_score:
    if score >= 90:
        students_grade.append('A')
    elif score >= 70:
        students_grade.append('B')
    else:
        students_grade.append('C')

print(students_grade)
