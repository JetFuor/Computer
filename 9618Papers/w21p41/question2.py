from turtle import width


class Picture():
    #Private Description        STRING
    #Private Width              INTEGER
    #Private Height             INTEGER
    #Private FrameColour        STRING

    def __init__(self, Description, Width, Height, FrameColour):
        self.Description = Description
        self.Width = Width
        self.Height = Height
        self.FrameColour = FrameColour

    def GetDescription(self):
        return self.Description

    def GetWidth(self):
        return self.Width

    def GetHeight(self):
        return self.Height

    def GetFrameColour(self):
        return self.FrameColour

    def SetDescription(self, NDescription):
        self.Description = NDescription

def ReadData(picturearray):
    try:
        with open("Pictures.txt", "r") as f:
            picturecount = 0
            description = f.readline().strip()
            while description != "":
                width = int(f.readline().strip())
                height = int(f.readline().strip())
                black = f.readline().strip()
                newpicture = Picture(description, width, height, black)
                picturearray[picturecount] = newpicture
                picturecount += 1
                description = f.readline().strip()
        return picturecount, picturearray
    except IOError:
        print("File cannot be found.")


picturearray = [Picture("", 0, 0, "") for i in range(100)]

picturecount, picturearray = ReadData(picturearray)

framecolor = input("Input the color of the frame: ")
maxwidth = int(input("Input the max width: "))
maxheight = int(input("Input the max height: "))

for i in range(picturecount):
    currentpicture = picturearray[i]
    if currentpicture.GetFrameColour().lower() == framecolor.lower():
        if currentpicture.GetWidth() <= maxwidth:
            if currentpicture.GetHeight() <= maxheight:
                print(currentpicture.GetDescription() + " " + str(currentpicture.GetWidth()) + " " + str(currentpicture.GetHeight()))

