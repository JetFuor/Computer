A = input()
B = input()

if A == "1" and B == "1":
    carry = "1"
else:
    carry = "0"

if (A == "1" and B == "0") or (A == "0" and B == "1"):
    sum = "1"
else:
    sum = "0"

print("C = " + carry)
print("S = " + sum)