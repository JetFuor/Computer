
def insertionsort(list):
    for i in range(1, len(list)):
        while i != 0:
            if list[i] < list[i-1]:
                temp = list[i]
                list[i] = list[i-1]
                list[i-1] = temp
                i = i - 1
            else:
                break
                
    print(list)

numbers = [3,6,2,9,4,77,22,17,96,43,87,223,5,76]
insertionsort(numbers)