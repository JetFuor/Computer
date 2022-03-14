from os import link


class node():
    def __init__(self, data, nextnode):
        self.data = data
        self.nextnode = nextnode

def outputNodes(linkedList, startpointer):
    currentnode = linkedList[startpointer]
    print(str(currentnode.data))
    while currentnode.nextnode != -1:
        currentnode = linkedList[currentnode.nextnode]
        print(str(currentnode.data))

def addNode(linkedList, startpointer, emptyList):
    newdata = int(input("Input the new data: "))
    currentendnode = linkedList[startpointer]
    while currentendnode.nextnode != -1:
        locationendnode = currentendnode.nextnode
        currentendnode = linkedList[currentendnode.nextnode]
    if emptyList != -1:
        linkedList[locationendnode] = node(currentendnode.data, emptyList)
        replacingnode = linkedList[emptyList]
        linkedList[emptyList] = node(newdata, -1)
        emptyList = replacingnode.nextnode
        return True
    else:
        return False
    
    # take node place we are changing and mess it up
    # Take the end of the current node line and update to go to next one


linkedList = [node(1,1), node(5,4), node(6,7), node(7,-1), node(2,2), node(0,6), node(0,8), node(56,3), node(0,9), node(0,-1)]
startpointer = 0
emptyList = 5

outputNodes(linkedList, startpointer)
success = addNode(linkedList, startpointer, emptyList)
if success:
    print("Node was added")
else:
    print("Failed add node")
outputNodes(linkedList, startpointer)




