from operator import itemgetter
from tracemalloc import start


linkedlist = [27, 19, 36, 42, 16, 24, None, None, None, None, None, None]
linkedlistpointers = [-1, 0, 1, 2, 3, 4, 7, 8, 9, 10, 11, -1]
startpointer = 5
nullpointer = -1
heapstartpointer = 6

def find(itemSearch):
    found = False
    itempointer = startpointer
    while itempointer != nullpointer and not found:
        if linkedlist[itempointer] == itemSearch:
            found = True
        else:
            itempointer = linkedlistpointers[itempointer]
    if itempointer != -1:
        print("Item found")
    else:
        print("Item not found")

def add(value):
    global startpointer, heapstartpointer, linkedlistpointers
    if heapstartpointer == nullpointer:
        print("List is full")
    else:
        temppointer = startpointer
        startpointer = heapstartpointer
        heapstartpointer = linkedlistpointers[heapstartpointer]
        linkedlist[startpointer] = value
        linkedlistpointers[startpointer] = temppointer

def deletemine(value):
    i = -1
    for i in range(heapstartpointer):
        if linkedlist[i] == value:
            node = i
            break
    if startpointer == nullpointer or i == nullpointer:
        print("List empty or item not found")
    else:
        linkedlist[node] = None
        for i in range(heapstartpointer):
            if node == linkedlistpointers[i]:
                linkedlistpointers[i] = linkedlistpointers[node]
                break
        linkedlistpointers[node] = None

def deleteproper(item):
    global heapstartpointer
    if startpointer == nullpointer:
        print("Linked list empty")
    else:
        index = startpointer
        while linkedlist[index] != item and index != nullpointer:
            oldindex = index
            index = linkedlistpointers[index]
        if index == nullpointer:
            print("Item not found")
        else:
            temppointer = linkedlistpointers[index]
            linkedlistpointers[index] = heapstartpointer
            heapstartpointer = index
            linkedlistpointers[oldindex] = temppointer

print(linkedlist)
print(linkedlistpointers)
deleteproper(42)
print(linkedlist)
print(linkedlistpointers)
add(1)
print(linkedlist)
print(linkedlistpointers)