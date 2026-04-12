import time

def checkbalance(balance):
    print("\n\n-------------------------------------------------")
    print(f"\tYour remaining balance is {balance:.2f}")
    print("-------------------------------------------------\n")


def withdraw(balance):
    while True:
        try:
            amount = float(input("Enter amount to withdraw: "))

            if amount > balance:
                print("\nInsufficient funds")

            elif amount <= 0:
                print("\nAmount must be greater than 0") 

            else:
                loading()
                balance -= amount
                print("\nWithdrawal Successful!")
                return balance

            print("\n1. Check Current Balance")
            print("2. Withdraw Again")
            print("3. Exit")

            option = input("Choose an option: ")

            if option == '1':
                checkbalance(balance)

            elif option == '2':
                continue

            elif option == '3':
                print("Thank you for using our bank!")
                exit()

            else:
                print("Invalid option. Returning to withdrawal.")

        except ValueError:
            print("\nInvalid input. Please enter numbers only.")

def loading():
    print("\nLoading", end="")
    for i in range(3):
        print(".", end="")
        time.sleep(1)
    print()

balance = 1000

while True:
    print("------------------------------------")
    print("\tWelcome to Abank")
    print("------------------------------------")

    print("\t1. Check My Balance")
    print("\t2. Withdraw")
    print("\t3. Exit")

    choice = input("\tEnter your choice: ")

    if choice == '1':
        loading()
        checkbalance(balance)  

    elif choice == '2':
        loading()
        balance = withdraw(balance)

    elif choice == '3':
        loading()
        print("Thank you for using our bank!")
        break
    else:
        loading()
        print("\nInvalid input, Please try again!")