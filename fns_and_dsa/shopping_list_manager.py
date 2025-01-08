def display_menu():
    print("Shopping List manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View items")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            item  = input("Enter the item name: ")
            shopping_list.append(item)
        elif choice == "2":
            item = input("Enter the item you want to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print(f"{item} not found in the shopping list.")
        elif choice == "3":
            for item in shopping_list:
                print(item)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()