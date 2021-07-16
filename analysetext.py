import string

punc = string.punctuation


def splitwords():
    with open("comments.txt", "r") as old:
        for line in old:
            words = line.split(" ")
            for word in words:
                deleted = 0
                for i in range(len(word)):
                    letter = word[i-deleted]
                    if punc.find(letter) != -1:
                        word = word[:i-deleted] + word[i+1-deleted:]
                        deleted += 1
                    elif letter == "\n":
                        word = word[:len(word)-1]
                if word != "\n" and word != "":
                    with open("updated_lines.txt", "a") as new:
                        new.write(word + "\n")

def countwords():
    with open("updated_lines.txt", "r") as f:
        # Has list, go through and find the word
        # If word not found, increment the 2nd one
        countlist = [[0 for i in range(2)] for j in range(1000)]
        for word in f:
            word = word[:len(word)-1]
            listindex = 0
            found = False
            compareword = countlist[listindex][0]
            while not found and listindex != len(countlist) and compareword != 0:
                if countlist[listindex][0].upper() == word.upper():
                    found = True
                else:
                    listindex += 1
                compareword = countlist[listindex][0]
            if found == False:
                countlist[listindex][0] = word
                countlist[listindex][1] = countlist[listindex][1] + 1
            else:
                countlist[listindex][1] = countlist[listindex][1] + 1
    for i in range(len(countlist)):
        if countlist[i][0] != 0:
            print(countlist[i][0] + " " + str(countlist[i][1]))



def main():
    splitwords()
    countwords()

main()