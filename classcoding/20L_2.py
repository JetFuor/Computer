import pickle
import datetime

class student:
    def __init__(self):
        self.name = ""
        self.registerNumber = 0
        self.dateOfBirth = datetime.datetime.now()
        self.fullTime = True


def new_record():
    studentRecord = student()
    with open('studentfile.DAT', 'ab') as studentFile:
        print("Please enter student details")
        studentRecord.name = input("Please enter student name: ")
        studentRecord.registerNumber = int(input("Please enter student's register number: "))
        year = int(input("Please enter student's year of birth YYYY: "))
        month = int(input("Please enter student's month of birth MM: "))
        day = int(input("Please enter student's day of birth DD: "))
        studentRecord.dateOfBirth = datetime.datetime(year, month, day)
        studentRecord.fullTime = bool(input("Please enter 1 for full-time or 0 for part-time: "))
        pickle.dump(studentRecord, studentFile)
        print(studentRecord.name, studentRecord.registerNumber, studentRecord.dateOfBirth, studentRecord.fullTime)

def read_records():
    with open('newstudentfile.DAT', 'rb') as studentFile:
        try:
            studentRecord = pickle.load(studentFile)
        except:
            print("File is empty.")
            studentRecord = ""
        while studentRecord != "":
            print(studentRecord.name, studentRecord.registerNumber, studentRecord.dateOfBirth, studentRecord.fullTime)
            try:
                studentRecord = pickle.load(studentFile)
            except EOFError:
                print("Reached EOF")
                studentRecord = ""
        
while True:
    task = input("Type in new or read to add a new record or read a record: ")
    if task == "new":
        new_record()
    elif task == "read":
        read_records()
    else:
        print("Not viable task.")
    if input("If you want to do another one, type Y: ") != "Y":
        break