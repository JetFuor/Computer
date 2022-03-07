
queue = [None for i in range(3)]
frontPointer = 0
rearPointer = -1
queueFull = len(queue)
queueLength = 0

def enqueue(number):
    global rearPointer, queueLength
    if queueFull == queueLength:
        print("Queue is full")
    else:
        rearPointer = (rearPointer + 1) % queueFull
        queue[rearPointer] = number
        queueLength += 1

def dequeue():
    global frontPointer, queueLength
    if queueLength == 0:
        print("Queue is empty")
    else:
        print(queue[frontPointer])
        frontPointer = (frontPointer + 1) % queueFull
        queueLength -= 1

enqueue(1)
enqueue(2)
enqueue(3)
dequeue()
dequeue()
enqueue(4)
enqueue(5)

if rearPointer >= frontPointer:
    print(queue[frontPointer:rearPointer + 1])
elif queueLength == 0:
    print("Nothing in queue")
else:
    print(queue[frontPointer:] + queue[:rearPointer + 1])