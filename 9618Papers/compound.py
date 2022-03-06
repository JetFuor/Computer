
# If 5% interest, written as 1.05

def compound(starting, years, interest):
    if years == 0:
        return starting
    else:
        return compound(starting * interest, years - 1, interest)

print(compound(127, 8, 1.08))