
def insertionsort(list):
    comparisons = 0
    for i in range(1, len(list)):
        while i != 0:
            comparisons += 1
            if list[i] < list[i-1]:
                temp = list[i]
                list[i] = list[i-1]
                list[i-1] = temp
                i = i - 1
            else:
                break
                
    print(list)
    print("Number of comparisons is " + str(comparisons))

def bubblesort(list):
    comparisons = 0
    no_swaps = False
    unsorted_numbers = len(list)

    while no_swaps == False:
        no_swaps = True
        for i in range(0, unsorted_numbers-1):
            comparisons += 1
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
                no_swaps = False
        unsorted_numbers = unsorted_numbers - 1

    print(list)
    print("Number of comparisons is " + str(comparisons))

numbers = [3,6,2,9,4,77,22,17,96,43,87,223,5,76]
sorted = [1,2,3,4,5,6,7,8,9]
bubblesort(sorted)
insertionsort(sorted)