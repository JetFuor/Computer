# 0, 1, 1, 2, 3, 5, 8, 13 
# Returning the element there, give placement number

def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1 
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(4))