
def bubblesort(list):
    no_swaps = False
    unsorted_numbers = len(list)

    while no_swaps == False:
        no_swaps = True
        for i in range(0, unsorted_numbers-1):
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
                no_swaps = False
        unsorted_numbers = unsorted_numbers - 1

    print(list)

numbers = [3,6,2,9,4,77,22,17,96,43,87,223,5,76]
bubblesort(numbers)