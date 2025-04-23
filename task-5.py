val = int(input("Enter a number: "))

def factorial(val):
    if val < 2:
        return 1
    else:
        return val * factorial(val - 1)

print("Factorial of", val, "is", factorial(val))
