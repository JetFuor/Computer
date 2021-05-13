# students : ARRAY[0:8]
# variables : ARRAY[0:2]
# name, email, dateOfBirth, spaces : STRING
# i, namegap, emailgap : INTEGER

students = []

for i in range(9):
    students.append("")

for i in range(len(students)):
    name = input("Input the student's name: ")
    email = input("Input the student's email: ")
    dateOfBirth = input("Input the student's date of the birth: ")
    students[i] = name + "*" + email + "*" + dateOfBirth

spaces = "                                                         "
print("Name" + spaces[:12] + "Email" + spaces[:20] + "Date Of Birth")
for student in students:
    variables = student.split("*")
    namegap = 16 - len(variables[0])
    emailgap = 25 - len(variables[1])
    print(variables[0] + spaces[:namegap] + variables[1] + spaces[:emailgap] + variables[2])