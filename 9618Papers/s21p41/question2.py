
def linearSearch(searchnumber, arrayData):
    for number in arrayData:
        if number == searchnumber:
            return True
    return False

def bubblesort(arrayData):
    for x in range(len(arrayData)):
        for y in range(len(arrayData)-1):
            if arrayData[y] < arrayData[y+1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y+1]
                arrayData[y+1] = temp


arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

bubblesort(arrayData)

print(arrayData)

""" searchnum = int(input("Input the number you want to search for: "))
found = linearSearch(searchnum, arrayData)
if found:
    print("Value was found")
else:
    print("Value not found") """

