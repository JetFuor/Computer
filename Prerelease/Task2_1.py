# stuID, email, dob : STRING
# keepgoing : CHAR

with open("students.txt","w") as f:
    keepgoing = "y"
    while keepgoing == "y":
        stuID = input("Input the Student ID with 2 letters followed by 4 characters: ")
        email = input("Input the email of the student: ")
        dob = input("Input the date of birth with a DDMMYY format: ")
        f.write(stuID + email + dob + "\n")
        keepgoing = input("Would you like to continue? y/n: ")
