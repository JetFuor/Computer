import pickle
import datetime
class student:
    def __init__(self):
        self.name = ""
        self.registerNumber = 0
        self.dateOfBirth = datetime.datetime.now()
        self.fullTime = True

count = 1

def new_record():
    global count
    studentRecord = student()
    with open('students' + str(count) + ".DAT", 'wb') as studentFile:
        print("Please enter student details")
        studentRecord.name = input("Please enter student name: ")
        studentRecord.registerNumber = int(input("Please enter student's register number: "))
        year = int(input("Please enter student's year of birth YYYY: "))
        month = int(input("Please enter student's month of birth MM: "))
        day = int(input("Please enter student's day of birth DD: "))
        studentRecord.dateOfBirth = datetime.datetime(year, month, day)
        studentRecord.fullTime = bool(input("Please enter True for full-time or False for part-time: "))
        pickle.dump(studentRecord, studentFile)
        print(studentRecord.name, studentRecord.registerNumber, studentRecord.dateOfBirth, studentRecord.fullTime)

    with open('students' + str(count) + ".DAT", 'rb') as studentFile:
        studentRecord = pickle.load(studentFile)
        print(studentRecord.name, studentRecord.registerNumber, studentRecord.dateOfBirth, studentRecord.fullTime)

    count +=1

def read_records():
    recordnum = input('Which number record do you want: ')
    with open('students' + str(recordnum) + ".DAT", 'rb') as studentFile:
        studentRecord = pickle.load(studentFile)
        print(studentRecord.name, studentRecord.registerNumber, studentRecord.dateOfBirth, studentRecord.fullTime)

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