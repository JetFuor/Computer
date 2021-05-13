# searchID, fileline, email : STRING
# found : BOOLEAN

searchID = input("Input the student ID: ")
found = False

with open("students.txt","r") as f:
    fileline = f.readline()
    while found == False and fileline != "":
        if fileline[:6] == searchID:
            email = fileline[6:(len(fileline)-7)]
            print(email)
            found = True
        else:
            fileline = f.readline()

if found == False:
    print("No student found.")
