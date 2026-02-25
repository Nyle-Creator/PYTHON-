def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

while True:
    
    print("\nSelect operation.")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5):")

    if choice == "5":
        print("Thank you for using my calculator :)")
        break

    try:
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))

        if choice == "1":
                print(num1, "+", num2, '=', add(num1, num2))
        elif choice == "2":
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == "3":
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == "4":
            print(num1, "/", num2, "=", divide(num1, num2))
        else:
            print("Invalid Input! Please choose 1-4.")

    except ValueError:
            print("Invalid input! Please enter numbers only.")

