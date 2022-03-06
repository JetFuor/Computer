def InsertionSort(TheData):
    for count in range(len(TheData)):
        DataToInsert = TheData[count]
        inserted = 0
        nextvalue = count - 1
        while (nextvalue >= 0 and inserted != 1):
            if DataToInsert < TheData[nextvalue]:
                TheData[nextvalue + 1] = TheData[nextvalue]       
                nextvalue = nextvalue - 1
                TheData[nextvalue + 1] = DataToInsert
            else:
                inserted = 1

def printdata(TheData):
    for number in TheData:
        print(number)

def finddata(TheData):
    searchnum = int(input("Input the number you want to find: "))
    for data in TheData:
        if searchnum == data:
            print("found")
            return True
    print("not found")
    return False

TheData = [20, 3, 4, 8, 12, 99, 4, 26, 4]

finddata(TheData)
finddata(TheData)
""" print("Before sorting: ")
printdata(TheData)
InsertionSort(TheData)
print("After sorting: ")
printdata(TheData) """
