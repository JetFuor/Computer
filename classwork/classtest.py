
binarynum = input("Input your binary number: ")

mantissa = binarynum[:8]
exponent = binarynum[8:]

# denarymantissa = int(mantissa[0]) * -1 + int(mantissa[1]) * 1/2 2**-1 + int(mantissa[2]) * 1/4 2**-2 + int(mantissa[3]) * 1/8 2**-3 + int(mantissa[4]) * 1/16 + int(mantissa[5]) * 1/32 + int(mantissa[6]) * 1/64 + int(mantissa[7]) * 1/128
denarymantissa = int(mantissa[0]) * -1
for i in range(1,8):
    denarymantissa = denarymantissa + int(mantissa[i]) * 2**(i*-1)

denaryexponent = int(exponent[0]) * -8 + int(exponent[1]) * 4 + int(exponent[2]) * 2 + int(exponent[3]) * 1

denarynum = denarymantissa * 2**denaryexponent

print(str(denarynum))

if binarynum[0] == "0" and binarynum[1] == "1" or binarynum[0] == "1" and binarynum[1] == "0":
    print("Normalised.")
else:
    print("Not normalised.")