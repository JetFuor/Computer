# students : ARRAY[0:8,0:4]
# spaces : STRING
# i, namegap, emailgap, dobgap, studentIDgap : INTEGER

students = []

for i in range(9):
    students.append([])

for i in range(9):
    students[i].append(input("Input the student's name: "))
    students[i].append(input("Input the student's email: "))
    students[i].append(input("Input the student's date of birth: "))
    students[i].append(input("Input the student's student ID: "))
    students[i].append(input("Input the student's tutor ID: "))

print("")
print("Here are all the students in a table with headers.")

spaces = "                                                                             "

print("Name" + spaces[:12] + "Email" + spaces[:20] + "Date of birth" + spaces[:5] + "StudentID" + spaces[:5] + "TutorID")

for i in range(len(students)):
    namegap = 16 - len(students[i][0])
    emailgap = 25 - len(students[i][1])
    dobgap = 18 - len(students[i][2])
    studentIDgap = 14 - len(students[i][3])
    print(students[i][0] + spaces[:namegap] + students[i][1] + spaces[:emailgap] + students[i][2] 
            + spaces[:dobgap] + students[i][3] + spaces[:studentIDgap] + students[i][4])