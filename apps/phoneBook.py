phone_book = {}

while True:
    print("\nPhone Book")
    print("1. Add a Contact")
    print("2. Search for a Contact")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter contact name: ")
        number = input("Enter contact number: ")

        phone_book[name] = number
    
    elif choice == '2':

        name = input("Enter contact name: ")
        number = phone_book.get(name, "Not Found")
        print(f"Contact number is : {number}")
    elif choice == "3":

        print("GoodBye!")
        break
    else:
        print("Invalid option. Please try again")