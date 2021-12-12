"""
class Student:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

stu_1 = Student('Tom', 'Dwan')
stu_2 = Student('Sarah', 'Yee')
"""

#Goal: Binary -> denary 2s compliment
#8 bits mantissa, 4 bits exponent
#tell user if its normalized

#ex: 01010001 0100
#user_num = input("Input a 12 bit binary number:\n")
#ex: 10101000 0010
#if start w 01 and positive = normalized
#if start w 10 and negative = normalized

user_num = "001100000001"
exponent = 0
final_num = 0
if len(user_num) == 12:
    if user_num[8] == "1":
        exponent = -8
    for i in range(1,3):
        if user_num[8 + i] == "1":
            exponent += 8/(2**i)
    if user_num[0] == "1":
        final_num = -(2**exponent)
    for n in range(1,8):
        if user_num[n] == "1":
            final_num += 2**(exponent-n)
else:
    print("Not valid input")
    
print(exponent)
print(final_num)
if (user_num[0:2] == "01"):
    print("It is normalized.")
elif(user_num[0:2] == "10"):
    print("It is normalized.")
else:
    print("It is not normalized.")