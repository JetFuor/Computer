def addstudent():
    # stuID, email, dob : STRING
    # nextstudent : CHAR

    with open("students.txt","a") as f:
        nextstudent = "y"
        while nextstudent == "y":
            stuID = input("Input the Student ID with 2 letters followed by 4 characters: ")
            email = input("Input the email of the student: ")
            dob = input("Input the date of birth with a DDMMYY format: ")
            f.write(stuID + email + dob + "\n")
            nextstudent = input("Would you like to continue? y/n: ")

def searchstudent():
    # searchID, fileline, stuID : STRING
    # i : INTEGER
    # found : BOOLEAN

    found = False

    searchID = input("Input substring: ")

    with open("students.txt","r") as f:
        fileline = f.readline()
        while fileline != "":
            stuID = fileline[:6]
            for i in range(7-len(searchID)):
                if searchID == stuID[i:i+len(searchID)]:
                    print(fileline)
                    found = True
            fileline = f.readline()

    if found == False:
        print("No one found.")

# command : STRING
# keepgoing : CHAR

keepgoing = "y"

while keepgoing == "y":
    command = input("Enter add or search to either add a student or search for a studentID: ")
    if command == "add":
        addstudent()
    elif command == "search":
        searchstudent()
    else:
        print("Command not available.")
    keepgoing = input("Would you like to input another command? y/n: ")