# students : ARRAY[0:8,0:4]
# searchingname : STRING
# i : INTEGER
# found : BOOLEAN

students = []

for i in range(9):
    students.append([])

for i in range(9):
    students[i].append(input("Input the student's name: "))
    students[i].append(input("Input the student's email: "))
    students[i].append(input("Input the student's date of birth: "))
    students[i].append(input("Input the student's student ID: "))
    students[i].append(input("Input the student's tutor ID: "))
    print("Student completed.")

searchingname = input("Who are you searching for: ")

found = False
i = 0

while found == False and i < len(students):
    if students[i][0] == searchingname:
        print(students[i][1])
        found = True
    else:
        i = i + 1

if found == False:
    print("No students found.")