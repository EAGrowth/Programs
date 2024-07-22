def show_balance(balance):

    print(f"Your balance is ${balance:.2f}")
    print(" ")

def deposit():

    amount = float(input("Enter an amount to be deposited: "))
    print(" ")
    if amount < 0:
        print(" ")
        print("That's not a valid amount")
        print(" ")
        return 0
    else:
        return amount

def withdraw(balance):

    amount = float(input("Enter amount to be withdrawn: "))
    print(" ")

    if amount > balance:

        print("Insufficient funds")
        print(" ")
        return 0
    elif amount < 0:

        print("Amount must be greater than 0")
        print(" ")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("Banking Program:   ")
        print(" ")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print(" ")
        decision = input("Enter your Decision (1-4): ")
        print(" ")

        if decision == '1':
            show_balance(balance)
        elif decision == '2':
            balance += deposit()
        elif decision == '3':
            balance -= withdraw(balance)
        elif decision == '4':
            is_running = False
        else:
            print(" ")
            print("That is not a valid decision")
            print(" ")


    print("Ended")


if __name__ == '__main__':
    main()
