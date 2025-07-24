pin = 0
account = {}    #stores all the user account in this dictionary


def bankAccount():
    while True:
        choice = int(input("""________________________
Bank System
[1] Create Account
[2] Login Account  
>> """))
        if choice == 1:
            createAcc()
        elif choice == 2:
            loginAcc()
        else:
            print("That's not an option"
                  "\n________________________")

def createAcc():
    pin = int(input("Create 4-digit PIN: "))

    if pin in account:
        print("PIN already exists!")
    else:
        print("Account Created!")
        account[pin] = 0
        account.update({pin : 0})   #adds the user's pin to the dictionary


def loginAcc():
    pin = int(input("Enter 4-digit PIN: "))

    if pin in account:
        bankMenu(pin)  #this function will go to your personal account
    else:
        print(f"This account {pin} doesn't exist! Please create account!")


def bankMenu(pin):

    print(account)
    choice = int(input(f"""
________________________
Bank System - {pin}    
[1] Withdraw
[2] Deposit
[3] Check Savings
[4] Exit
>> """))

    if choice == 1:
        withdraw(pin)
    elif choice == 2:
        deposit(pin)
    elif choice == 3:
        checkSavings(pin)
    elif choice == 4:
        bankAccount()
    else:
        print("That's not an option"
              "\n________________________")


def withdraw(pin):
    print(f"___________________________"
          f"\nSavings: {account[pin]}")
    withdrawMoney = float(input("Withdraw: "))

    while withdrawMoney > account[pin]:             #prints while the amount is more than the stored money
        print(f"Savings: {account[pin]}")
        print("Insufficient Amount\n"               
              "___________________________")
        withdrawMoney = float(input("Withdraw: "))
    if withdrawMoney <= account[pin]:
        account[pin] -= withdrawMoney               #subtracts withdrawMoney to the value of user's account
        print(f"Withdrew: {withdrawMoney}\n")
        bankMenu(pin)


def deposit(pin):
    savings = float(input("Amount: "))
    account[pin] += savings         #adds withdrawMoney to the value of user's account
    print(f"___________________________"
          f"\nNew Savings: {account[pin]}\n"
          f"___________________________")
    bankMenu(pin)


#prints user's savings
def checkSavings(pin):
    print(f"___________________________"
          f"\nPIN: {pin}"
          f"\nYour Savings: {account[pin]}\n"
          f"___________________________")


#first interface in this system  to access the bankAccount(),
#allowing the system to function properly
enter = input("Type OPEN to enter : ")
x = enter.upper()

if x == "OPEN":
    bankAccount()