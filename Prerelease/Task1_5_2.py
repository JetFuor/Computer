# i : INTEGER

def printstudents(students):

    print("Here are all the students.")

    for i in range(len(students)):
        if students[i][1] != "":
            print(students[i])