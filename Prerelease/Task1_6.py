# choice, searchstring : STRING
# searchtype, i : INTEGER
# valid, found : BOOLEAN

def search(students):
    print("What type of data would you like to search for? Choose from name, email, date of birth, studentID or tutorID.")

    valid = False
    searchtype = 9

    while valid == False:
        choice = input()
        if choice == "name":
            searchtype = 0
        elif choice == "email":
            searchtype = 1
        elif choice == "date of birth":
            searchtype = 2
        elif choice == "studentID":
            searchtype = 3
        elif choice == "tutorID":
            searchtype = 4
        else:
            print("Not a choice. Retry inputting.")
        if searchtype != 9:
            valid = True

    searchstring = input("Input the data you want to search for: ")

    found = False

    for i in range(len(students)):
        if searchstring == students[i][searchtype]:
            print(students[i])
            found = True
    
    if found == False:
        print("No students found.")
    