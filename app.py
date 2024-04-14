print("Welcome to Shopping list! \n")

# Create a list to store the items
shopping_list = []

# Create a function to add items to the list
def add_item():
    item = input("What item would you like to add? ")
    shopping_list.append(item)
    print(f"{item} has been added to the list. \n")

# Create a function to remove items from the list
def remove_item():
    item = input("What item would you like to remove? ")
    shopping_list.remove(item)
    print(f"{item} has been removed from the list. \n")

# Create a function to show the items in the list
def show_list():
    print("Here is your shopping list: \n")
    for item in shopping_list:
        print(item)
    print("\n")

# Create a function to clear the list
def clear_list():
    shopping_list.clear()
    print("Your list has been cleared. \n")

# Create a function to show the menu

def show_menu():
    print("Menu: \n")
    print("1. Add item")
    print("2. Remove item")
    print("3. Show list")
    print("4. Clear list")
    print("5. Exit \n")

# Create a loop to show the menu and get user input
while True:
    show_menu()
    choice = input("What would you like to do? ")
    if choice == "1":
        add_item()
    elif choice == "2":
        remove_item()
    elif choice == "3":
        show_list()
    elif choice == "4":
        clear_list()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again. \n")

print("Thank you for using Shopping list! \n")