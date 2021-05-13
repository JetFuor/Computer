# matchinglist : ARRAY[0:8]
# searchmonth, studate : STRING
# i : INTEGER
# found : BOOLEAN

def searchbirthmonth(students):

    searchmonth = input("Input the first 3 letters of the month you want to search for, first letter capitalized: ")

    found = False

    matchinglist = []

    for i in range(len(students)):
        studate = students[i][2]
        studate = studate[-8:]
        if searchmonth == studate[:3]:
            matchinglist.append(students[i][0])
            found = True

    if found == False:
        print("No students found with this birth month.")
    else:
        print(matchinglist)
