# matchinglist : ARRAY[0:8]
# variables : ARRAY[0:2]
# searchmonth, student, studate : STRING
# found : BOOLEAN

def searchbirthmonth(students):

    searchmonth = input("Input the first 3 letters of the month you want to search for, first letter capitalized: ")

    found = False

    matchinglist = []

    for student in students:
        studate = student[-7:]
        if searchmonth == studate[:3]:
            variables = student.split("*")
            matchinglist.append(variables[0])
            found = True

    if found == False:
        print("No students found.")
    else:
        print(matchinglist)
