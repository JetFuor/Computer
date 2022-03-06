
class HiddenBox():
    # BoxName       String
    # Creator       String
    # DateHidden    Datetime
    # GameLocation  String
    # LastFinds     Array[10][2] of String
    # Active        Boolean

    def __init__(self, BoxName, Creator, DateHidden, GameLocation):
        self.BoxName = BoxName
        self.Creator = Creator
        self.DateHidden = DateHidden
        self.GameLocation = GameLocation
        self.LastFinds = [["" for i in range(2)] for j in range(10)]
        self.Active = False

    def GetBoxName(self):
        return self.BoxName

    def GetGameLocation(self):
        return self.GameLocation

class PuzzleBox(HiddenBox):
    def __init__(self, BoxName, Creator, DateHidden, GameLocation, PuzzleText, Solution):
        super().__init__(BoxName, Creator, DateHidden, GameLocation)
        self.PuzzleText = PuzzleText    #String
        self.Solution = Solution        #String


def NewBox(TheBoxes):
    BoxName = input("Enter the name of the box: ")
    Creator = input("Enter the creator's name: ")
    DateHidden = input("Enter the date the box was hidden: ")
    Location = input("Enter the location of the box: ")
    TheBoxes.append(HiddenBox(BoxName, Creator, DateHidden, Location))


TheBoxes = [HiddenBox("", "", "", "") for i in range(10000)]
NewBox(TheBoxes)
