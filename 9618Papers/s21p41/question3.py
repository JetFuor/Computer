class TreasureChest():
    #private question      string
    #private answer        integer
    #private points        integer

    def __init__(self, question, answer, points):
        self.question = question
        self.answer = answer
        self.points = points
    
    def getQuestion(self):
        return self.question

    def checkAnswer(self, useranswer):
        if useranswer == self.answer:
            return True
        else:
            return False

    def getPoints(self, numattempts):
        if numattempts == 1:
            return int(self.points)
        elif numattempts == 2:
            return int(self.points) // 2
        elif numattempts == 3 or numattempts == 4:
            return int(self.points) // 4
        else:
            return 0


def readdata():
    global arrayTreasure
    try:
        with open("TreasureChestData.txt", "r") as f:
            arrayTreasure = []          #Array of TreasureChest
            question = f.readline().strip()
            while question != "":
                answer = f.readline().strip()
                points = f.readline().strip()
                newdata = TreasureChest(question, answer, points)
                arrayTreasure.append(newdata)
                question = f.readline().strip()
    except IOError:
        print("File not found")

readdata()
questionnum = int(input("Input question between 1 and 5: "))
if questionnum > 0 and questionnum < 6:
    question = arrayTreasure[questionnum-1]
    print(question.question)
    solved = False
    attempts = 0
    while solved == False:
        answer = input("Input the answer: ")
        attempts += 1
        solved = question.checkAnswer(answer)
    points = question.getPoints(attempts)
    print("You got " + str(points) + " points.")




         