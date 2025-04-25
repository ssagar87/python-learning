import math

#task 1
val = int(input("Enter a number: "))

def factorial(val):
    if val < 2:
        return 1
    else:
        return val * factorial(val - 1)

print("Factorial of", val, "is", factorial(val))

#task 2


try:
    num = float(input("Enter a number: "))

    if num <= 0:
        print("Please enter a positive number greater than 0 for sqrt and log calculations.")
    else:
        sqrt_val = math.sqrt(num)
        log_val = math.log(num)
        sine_val = math.sin(num)

        print(f"Square root of {num} is {sqrt_val}")
        print(f"Natural logarithm of {num} is {log_val}")
        print(f"Sine of {num} (in radians) is {sine_val}")

except ValueError:
    print("Invalid input. Please enter a valid number.")

