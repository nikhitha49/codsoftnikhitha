# Simple calculator

# Read two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Show choices
print("Choose an operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

choice = input("Enter 1, 2, 3, or 4: ")

# Perform calculation based on choice
if choice == "1":
    result = num1 + num2
    symbol = "+"
elif choice == "2":
    result = num1 - num2
    symbol = "-"
elif choice == "3":
    result = num1 * num2
    symbol = "*"
elif choice == "4":
    result = num1 / num2
    symbol = "/"
else:
    print("Invalid choice!")
    exit()

# Display the result
print(f"{num1} {symbol} {num2} = {result}")
