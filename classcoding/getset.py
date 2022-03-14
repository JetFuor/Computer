
class Addition:

    def __init__(self, f, s):
        if type(f) == int:
            self.first = f
        else:
            print("Nah first one ain't a number")
            self.first = None
        if type(s) == int:
            self.second = s
        else:
            print("Nah second one ain't a number")
            self.second = None

    def display(self):
        print("First number = " + str(self.first))
        print("Second number = " + str(self.second))
        print("Addition of two numbers = " + str(self.answer))

    def calculate(self):
        self.answer = self.first + self.second
    
    def setfirst(self, f):
        if type(f) == int:
            self.first = f
        else:
            print("Nah that ain't a number")
    
    def setsecond(self, s):
        if type(s) == int:
            self.first = s
        else:
            print("Nah that one ain't a number")

Five = Addition("n", 11)
Five.setfirst(2)
Five.calculate()
Five.display()