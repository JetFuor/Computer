folderList = 'E:/17th Bday'

while True:
    i = 0
    if folderList[i] == "/":
        folderList = folderList[:i] + "\\" + folderList[i + 1:] 
    if i == len(folderList):
        break

print(folderList)