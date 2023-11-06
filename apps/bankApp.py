# Defining a class named BankAccount which will represent a simple bank account
class BankAccount:
    # The initializer method to set up objects with an initial balance of 0
    def __init__(self):
        self.balance = 0  # Instance variable to keep track of the balance

    # Method to handle depositing money into the account
    def deposit(self, amount):
        self.balance += amount  # Adds the amount to the balance
        print(f"${amount} deposited. New balance is ${self.balance}.")

    # Method to handle withdrawing money from the account
    def withdraw(self, amount):
        if amount > self.balance:  # Checks if there are sufficient funds
            print("Insufficient funds.")
        else:
            self.balance -= amount  # Subtracts the amount from the balance
            print(f"${amount} withdrawn. New balance is ${self.balance}.")

    # Method to check the current balance of the account
    def get_balance(self):
        print(f"The current balance is ${self.balance}.")

# Function that encapsulates the bank account operations
def bank_account_app():
    account = BankAccount()  # Creates a new BankAccount object named 'account'

    # An infinite loop to keep the application running until the user decides to exit
    while True:
        # Printing the options for the user to choose from
        print("\n1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")

        # Getting user input to select an option
        choice = input("Choose an option: ")

        # Handling each option by calling the appropriate BankAccount method or exiting the loop
        if choice == '1':
            amount = float(input("Enter the amount to deposit: "))  # Getting the amount to deposit
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter the amount to withdraw: "))  # Getting the amount to withdraw
            account.withdraw(amount)
        elif choice == '3':
            account.get_balance()  # Displaying the balance
        elif choice == '4':
            print("Exiting Bank Account Manager.")  # Exiting message
            break  # Breaks out of the while loop to exit the app
        else:
            print("Invalid option. Please try again.")  # Handles invalid option input

# This is a common Python idiom. When the Python interpreter reads a source file, it executes all of the code found in it.
# Before executing the code, it defines a few special variables. For example, if the Python interpreter is running that
# module (the source file) as the main program, it sets the special __name__ variable to have a value "__main__".
# If this file is being imported from another module, __name__ will be set to the module's name.
if __name__ == "__main__":
    bank_account_app()  # Calls the function to start the application if this file is the main program
