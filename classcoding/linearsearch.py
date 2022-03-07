
def linear_search(target, list):
    found = False
    for i in range(len(list)):
        if list[i] == target:
            found = True
            print("It is found at position " + str(i+1))
            break

    if found == False:
        print("Not found.")
            

numbers = [3,6,2,9,4,77,22,17,96,43,87,223,5,76]
target = int(input("What number do you want to look for: "))
linear_search(target, numbers)