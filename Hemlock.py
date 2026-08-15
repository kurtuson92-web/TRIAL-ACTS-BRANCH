balance = 1000

def cash_in(amount):
    global balance
    balance += amount
    print(f"Cash in: ₱{amount}")
    print(f"New balance: ₱{balance}")

def withdraw(amount):
    global balance

    if amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        print(f"Withdraw: ₱{amount}")
        print(f"New balance: ₱{balance}")