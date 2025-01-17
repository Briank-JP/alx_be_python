from bank_account import BankAccount
import sys

def main():
    account  = BankAccount(0)
    
    if len(sys.argv) < 2:
        print("usage: python main-0.py <command>:<amount>")
        print("commands: deposit, withdraw, display")
        sys.exit(1)
        
    command, *params = sys.argv[1].split(":")
    amount = float(params[0]) if params else None
    
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited ${amount}. ")
        account.display_balance()
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew ${amount}.")
            account.display_balance()
        else:
            print("Insufficient funds")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")
        
if __name__ == "__main__":
    main()