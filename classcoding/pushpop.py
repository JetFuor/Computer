
def pop():
    global max, toppointer, item, stack
    if toppointer == -1:
        print("Stack is empty")
    else:
        item = stack[toppointer]
        toppointer = toppointer - 1

def push():
    global toppointer
    if toppointer < max - 1:
        stack[toppointer + 1] = item
        toppointer = toppointer + 1
    else:
        print("Stack is full")

stack = [0,1,2,3,4,None,None,None,None,None]
max = len(stack)
toppointer = 4
item = None

pop()
pop()
push()
for i in range(toppointer + 1):
    print(stack[i])





'''
for i in range(len(stack)):
        if stack[i] == None:
            toppointer = i - 1
            break
'''