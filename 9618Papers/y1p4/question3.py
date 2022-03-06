
def Enqueue(QueueData, NewData):
    global endpointer
    if endpointer != 20:
        QueueData[endpointer] = NewData
        endpointer += 1
        return True
    return False

def ReadFile():
    filename = input("Input the text file name: ")
    try:
        f = open(filename, "r")
        f.close()
    except:
        return -1
    with open(filename, "r") as f:
        notfull = True
        NewData = f.readline()
        while notfull == True and NewData != "":
            notfull = Enqueue(QueueData, NewData)
            NewData = f.readline()
        if notfull:
            return 1 
        else:
            return 2

def Remove(QueueData):
    global startpointer
    if QueueData[startpointer] != "" and QueueData[startpointer+1] != "":
        removedstring = QueueData[startpointer] + " " + QueueData[startpointer+1]
        QueueData[startpointer] = ""
        QueueData[startpointer+1] = ""
        startpointer += 2
        return removedstring
    else:
        return "No Items"

QueueData = ["" for i in range(20)]
startpointer = 0
endpointer = 0

returnvalue = ReadFile()
if returnvalue == 1:
    print("All items added")
elif returnvalue == 2:
    print("Queue is full")
else:
    print("File does not exist")

print(Remove(QueueData))