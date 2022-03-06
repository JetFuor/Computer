def fourDigits():
    number = int(input("Please input a 4 digit number: "))

    print(int(number/1000))
    print(int(number/100) - int(number/1000)*10)
    print(int((number % 100 - (number % 10)) / 10))
    print(number % 10)


fourDigits()