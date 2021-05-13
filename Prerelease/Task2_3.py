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