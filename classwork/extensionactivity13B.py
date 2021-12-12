ID = ""

while ID == "" and len(ID) <= 10:
    ID = input("Input your ID: ")
    if len(ID) > 10:
        ID = ""
        print("Retry. ID is too long.")
    else:
        for letter in ID:
            if (letter >= "a" and letter <= "z") or (letter >= "A" and letter <= "Z"):
                continue
            else:
                ID = ""
                print("Retry. Only alphabetic letters are allowed.")
                break

totalascii = 0
for letter in ID:
    totalascii += ord(letter)

result = totalascii % 1000 * 20 + 2000
print(result)
