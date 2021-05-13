# students : ARRAY[0:8]
# variables : ARRAY[0:2]
# studentName, email, dateOfBirth, searchingname : STRING
# i : INTEGER
# found : BOOLEAN

students = []

for i in range(9):
    students.append("")

for i in range(len(students)):
    studentName = input("Input the student's name: ")
    email = input("Input the student's email: ")
    dateOfBirth = input("Input the student's date of the birth: ")
    students[i] = studentName + "*" + email + "*" + dateOfBirth

searchingname = input("Input the name of the person whose email you want: ")

found = False
i = 0

while found == False and i < len(students):
    variables = students[i].split("*")
    if variables[0] == searchingname:
        print(variables[1])
        found = True
    else:
        i = i + 1

if found == False:
    print("No students found.")