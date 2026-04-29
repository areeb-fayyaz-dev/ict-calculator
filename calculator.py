# ============================================
#        Simple Calculator - ICT Lab Task
# ============================================

def calculator():
    print("=" * 40)
    print("       SIMPLE CALCULATOR")
    print("  Operations: +  -  *  /  %")
    print("=" * 40)

    # Get two integers from user
    num1 = int(input("\nEnter first integer:  "))
    num2 = int(input("Enter second integer: "))

    print("\n" + "-" * 40)
    print(f"  Results for {num1} and {num2}:")
    print("-" * 40)

    # Addition
    addition = num1 + num2
    print(f"  Addition       (+) : {num1} + {num2} = {addition}")

    # Subtraction
    subtraction = num1 - num2
    print(f"  Subtraction    (-) : {num1} - {num2} = {subtraction}")

    # Multiplication
    multiplication = num1 * num2
    print(f"  Multiplication (*) : {num1} * {num2} = {multiplication}")

    # Division
    if num2 != 0:
        division = num1 / num2
        print(f"  Division       (/) : {num1} / {num2} = {division:.2f}")
    else:
        print(f"  Division       (/) : Cannot divide by zero!")

    # Modulus
    if num2 != 0:
        modulus = num1 % num2
        print(f"  Modulus        (%) : {num1} % {num2} = {modulus}")
    else:
        print(f"  Modulus        (%) : Cannot mod by zero!")

    print("-" * 40)
    print("  Calculation complete!")
    print("=" * 40)


# Run the calculator
calculator()
