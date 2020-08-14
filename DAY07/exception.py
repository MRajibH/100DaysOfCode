import sys
try:
    x = int(input("Enter X: "))
    y = int(input("Enter Y: "))
except ValueError:
    print("Error: Invalid Input")
    sys.exit(1)


try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot Divide by Zero")
    sys.exit(1)
print(f'Result of {x}/{y} = {result}')
