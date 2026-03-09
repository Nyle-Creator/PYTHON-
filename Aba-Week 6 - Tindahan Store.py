import time

cart = []

def loading():
    print("\nLoading", end="")
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(1)
    print()

def AddItem():
    while True:
        item = input("\nAdd an item: ")

        if not item.replace(" ", "").isalpha():
            print("\nInvalid item name. Please enter valid names only.")
            continue
        
        while True:
                try:
                    price = float(input("Enter item price: "))
                    cart.append([item, price])
                    print(item, "added to cart! :)\n")
                    break
                except ValueError:
                    print("Invalid price. Try again.")

        again = input("\nAdd another item? (yes/no): ").lower()

        if again == "no":
            break
            
        
def ViewCart():
    if len(cart) == 0:
        print("Your cart is empty.")
    else:
        print("\nYour shopping cart:")
        total = 0
        for item in cart:
            print(item[0], "=",item[1])
            total += item [1]
        print("\nTotal:", total)

def RemoveItem():
    name = input("\nEnter item name to remove: ")

    for item in cart:
        if item[0] == name:
            cart.remove(item)
            print(name, "removed.")
            return

    print("Item not found.")
        
def Checkout():
    if len(cart) == 0:
        print("\nYour cart is empty. Nothing to checkout.")
        return

    print("\n----- Checkout -----")
    total = 0

    for item in cart:
        print(item[0], "=", item[1])
        total += item[1]

    print("Total amount:", total)

    confirm = input("Confirm purchase? (yes/no): ")

    if confirm.lower() == "yes":
        print("Purchase successful! Thank you for shopping.")
        cart.clear()
    else:
        print("Checkout cancelled.")

def menu():

    while True:

        print("\n--------------------------------------------------")
        print("\t\tTindahan Store")
        print("--------------------------------------------------")
        print("\t\t1.Add Item")
        print("\t\t2.View cart")
        print("\t\t3.Remove Item")
        print("\t\t4.Checkout")
        print("\t\t5.Exit")

        choice =(input("\nChoose an option: "))

        loading()

        if choice == "5":
            print("\nThank you for using my program :)")
            break
        
        if choice == "1":
            AddItem()
        elif choice == "2":
            ViewCart()
        elif choice == "3":
            RemoveItem()
        elif choice == "4":
            Checkout()
        else:
            print("Invalid choice.")
                

menu()