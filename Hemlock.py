balance = 1000
correct_pin = "1234"

pin = input("Enter PIN: ")

if pin != correct_pin:
    print("Incorrect PIN.")
    exit()

print("PIN accepted.")

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