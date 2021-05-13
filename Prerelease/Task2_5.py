# stuID, email, dob : STRING
# validcount, i : INTEGER
# valid : BOOLEAN

valid = False

while valid == False:
    stuid = input("Input the Student ID with 2 letters followed by 4 characters: ")
    if len(stuID) != 6:
        print("Not right length.")
    else:
        validcount = 0
        for i in range(2):
            if stuID[i] >= "A" and stuID[i] <= "Z":
                validcount = validcount + 1
        for i in range(2,6):
            if stuID[i] >= "0" and stuID[i] <="9":
                validcount = validcount + 1
        if validcount == 6:
            valid = True
        else:
            print("Invalid ID. Retry.")

email = input("Input the email of the student: ")

valid = False

while valid == False:
    dob = input("Input the date of birth with a DDMMYY format: ")
    if len(dob) != 6:
        print("Not right length. Retry.")
    else:
        if dob[0] < "0" or dob[0] > "3":
            print("Invalid date of birth. Retry.")
        elif dob[1] < "0" or dob[1] > "9":
            print("Invalid date of birth. Retry.")
        elif dob[2] < "0" or dob[2] > "1":
            print("Invalid date of birth. Retry.")
        elif dob[3] < "0" or dob[3] > "9":
            print("Invalid date of birth. Retry.")
        elif dob[4] < "0" or dob[4] > "9":
            print("Invalid date of birth. Retry.")
        elif dob[5] < "0" or dob[5] > "9":
            print("Invalid date of birth. Retry.")
        else:
            valid = True

with open("students.txt", "a") as f:
    f.write(stuID + email + dob + "\n")