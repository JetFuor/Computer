import pickle
import datetime
import os

class student:
    def __init__(self):
        self.name = ""
        self.registerNumber = 0
        self.dateOfBirth = datetime.datetime.now()
        self.fullTime = True

recordadded = False
newStudentRecord = student()

with open("newstudentfile.DAT", "wb") as newStudentFile:
    with open("studentfile.DAT", "rb") as studentFile:
        print("Please enter student details")
        newStudentRecord.name = input("Please enter student name: ")
        newStudentRecord.registerNumber = int(input("Please enter student's register number: "))
        year = int(input("Please enter student's year of birth YYYY: "))
        month = int(input("Please enter student's month of birth MM: "))
        day = int(input("Please enter student's day of birth DD: "))
        newStudentRecord.dateOfBirth = datetime.datetime(year, month, day)
        newStudentRecord.fullTime = bool(input("Please enter 1 for full-time or 0 for part-time: "))
        print(newStudentRecord.name, newStudentRecord.registerNumber, newStudentRecord.dateOfBirth, newStudentRecord.fullTime)

        while not recordadded:
            try:
                studentRecord = pickle.load(studentFile)
                if newStudentRecord.registerNumber > studentRecord.registerNumber:
                    pickle.dump(studentRecord, newStudentFile)
                else:
                    pickle.dump(newStudentRecord, newStudentFile)
                    recordadded = True
            except:
                pickle.dump(newStudentRecord, newStudentFile)
                recordadded = True

        while True:
            try:
                pickle.dump(studentRecord, newStudentFile)
                studentRecord = pickle.load(studentFile)
            except:
                break

# renaming and deleting files
'''
os.remove("studentfile.DAT")
os.rename("newstudentfile.DAT", "studentfile.DAT")
'''