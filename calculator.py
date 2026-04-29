# Simple Calculator

# Take two numbers from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calculate all operations
addition       = num1 + num2
subtraction    = num1 - num2
multiplication = num1 * num2

if num2 != 0:
    division = num1 / num2
    modulus  = num1 % num2
else:
    division = "Cannot divide by zero"
    modulus  = "Cannot divide by zero"

# Show results
print("Results:")
print("Addition       :", addition)
print("Subtraction    :", subtraction)
print("Multiplication :", multiplication)
print("Division       :", division)
print("Modulus        :", modulus)
