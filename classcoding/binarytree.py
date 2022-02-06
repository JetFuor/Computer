
tree = [[27, 1, 2], [19, 4, 6], [36, -1, 3], [42, -1, 5], [16, -1, 7], [89, 8, -1], [21, -1, -1], 
[17, -1, -1], [55, -1, -1]]

rootpointer = 0
nextfreepointer = 9

def search(number):
    itempointer = rootpointer
    while tree[itempointer][0] != number and (itempointer != -1):
        if tree[itempointer][0] > number:
            itempointer = tree[itempointer][1]
        else:
            itempointer = tree[itempointer][2]
    if itempointer == -1:
        print("Not found.")
    else:
        print(itempointer)

def add(number):
    global nextfreepointer
    itempointer = rootpointer
    while tree[itempointer][0] != number and (itempointer != -1):
        if tree[itempointer][0] > number:
            if tree[itempointer][1] == -1:
                break
            else:
                itempointer = tree[itempointer][1]
        else:
            if tree[itempointer][2] == -1:
                break
            else:
                itempointer = tree[itempointer][2]
    if tree[itempointer][0] == number:
        print("Item already present.")
    else:
        tree.append([number, -1, -1])
        if tree[itempointer][0] > number:
            tree[itempointer][1] = nextfreepointer
        else:
            tree[itempointer][2] = nextfreepointer
        nextfreepointer += 1
        print("Success")
        print(tree)

add(90)
add(91)
