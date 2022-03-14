
def binary_search(target, list):
    start = 0
    end = len(list)-1
    found = False
    while (end - start) >= 0:
        middle = int((start+end)/2)
        if target == list[middle]:
            found = True
            print("It is found at position " + str(middle+1))
            break
        elif target > list[middle]:
            start = middle + 1
        elif target < list[middle]:
            end = middle - 1
    if found == False:
        print("Not found.")

numbers = [1,5,8,9,23,32,43,66,77,86,89]

target = int(input("What number do you want to look for: "))

binary_search(target, numbers)