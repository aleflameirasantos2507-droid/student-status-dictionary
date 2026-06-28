student = {}

student['name'] = input('Name: ')
student['average'] = float(input(f"Average for {student['name']}: "))

if student['average'] < 7:
    student['status'] = 'Failed'
else:
    student['status'] = 'Passed'

for key, value in student.items():
    print(f'{key} --> {value}')
