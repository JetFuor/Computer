A = int(input())
B = int(input())
C = int(input())

Sum0 = A ^ B

Carry0 = A & B

Sum1 = Carry0 ^ C

Carry1 = Carry0 & C

Sum = Sum1

Carry = Carry0 or Carry1