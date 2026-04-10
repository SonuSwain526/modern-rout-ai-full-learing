class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = float(balance)

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"BankAccount(owner={self.owner}, balance={self.balance:.2f})"


def main():
    print("Welcome to the simple Bank App")
    name = input("Enter account owner name: ")
    account = BankAccount(name)

    while True:
        print("\nSelect option:")
        print("1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choice (1-4): ")
        if choice == "1":
            print(f"Current balance: ${account.get_balance():.2f}")
        elif choice == "2":
            amt = float(input("Deposit amount: "))
            try:
                account.deposit(amt)
                print(f"Deposited ${amt:.2f}. New balance ${account.get_balance():.2f}")
            except ValueError as ex:
                print("Error:", ex)
        elif choice == "3":
            amt = float(input("Withdraw amount: "))
            try:
                account.withdraw(amt)
                print(f"Withdrew ${amt:.2f}. New balance ${account.get_balance():.2f}")
            except ValueError as ex:
                print("Error:", ex)
        elif choice == "4":
            print("Thank you for using the Bank App. Goodbye!")
            break
        else:
            print("Invalid option. Please choose between 1 and 4.")


if __name__ == "__main__":
    main()
