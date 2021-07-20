image = "123.jpg"
templen = len(image) - 1
while True:
    if image[templen] == ".":
        break
    else:
        templen = templen - 1
print(image[templen:])