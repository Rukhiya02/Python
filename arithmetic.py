summation = 0
difference = 0
product = 0
quotient = 0
remainder = 0
try:

    Inum1 = input("enter the first number: ")
    Inum2 = input("enter the second number: ")

    num1 = float(Inum1)
    num2 = float(Inum2)
    summation = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    quotient = num1 / num2
    remainder = num1 % num2

except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")
    exit(1)
except ValueError as e:
    print(f"Value Error: {e}")
    exit(1)
except Exception as e:
    print(e)
    exit(1)
print(f"Sum: {summation}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Quotient: {quotient}")
print(f"Remainder: {remainder}")
