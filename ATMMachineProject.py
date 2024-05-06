# used libraries: datetime, sys, json
# Please note that if you don't have these modules installed,
# you maybe can't run this code on your device.
import datetime
import sys
import json
import time
# loading data:
# loading clients file:
x = open('data.json')
clients = json.load(x)
# loading categories file:
j = open('moneycategory.json')
categories = json.load(j)

ATMTotalMoney = 0

# calculating ATM total money by summing money categories:
for p, k in categories.items():
    product = int(p) * k
    ATMTotalMoney += product

OutputMoney = []
username_array, PIN_array, balance_array = [], [], []

# filling username, PIN, & balance arrays everytime we open the program with the modified json file:
for i, j in clients.items():
    username_array.append(i)
    PIN_array.append(clients[i]["PIN"])
    balance_array.append(clients[i]["balance"])

# Greeting:
print("Hello!, this is your local ATM machine")

# showing the current time:
print(f"it's {datetime.datetime.now()}")

# asking the user for username:
while True:
    user = str(input("Please enter the user name:"))
    if user in username_array:
        break

PIN = int(input("Please enter the PIN (4 digits) : "))
# check if correct PIN:
userindex = username_array.index(user)
try:
    PINindex = PIN_array.index(PIN)
except:
    print("Wrong PIN!")
    sys.exit()
if userindex != PINindex:
    print("Wrong PIN!")
    sys.exit()
else:
    userbalance = balance_array[userindex]
    # balance inquiry or withdraw
    print(f"Welcome {user}, Type the number of process you aim to:")
    print("1. Balance inquiry.\n2. Withdraw.")
    process = int(input())
    if process != 1 and process != 2:
        print("Undefined process!, Enter 1 for balance inquiry, 2 to withdraw.")
        process = int(input())
    if process == 1:
        # output user balance:
        print(f"Your current balance is: {userbalance}")
        print("Type the number of process you want to:")
        print("1. Withdraw.\n2. Quit.")
        while True:
            process2 = int(input())
            if process2 == 1 or process2 == 2:
                break
        if process2 == 2:
            print("Have a nice day!")
            sys.exit()

        elif process2 == 1:

            # Check if the required money is less than 5000 EGP
            while True:
                reqmoney = int(input("Enter the amount of money, maximum 5,000 EGP:"))
                if reqmoney <= 5000 and reqmoney > 0:
                    break

            if reqmoney <= 5000:
                # check if the required money is bigger than user balance:
                if reqmoney > userbalance:
                    print(f"You have only {userbalance}, Re-Enter the required amount of money:")
                    reqmoney = int(input())

                # check if the required money is less than ATM total balance:
                if reqmoney > ATMTotalMoney:
                    print(f"Sorry there is no enough money at the moment.\nThere is only {ATMTotalMoney}, would you like to change the required amount of money?")
                    process3 = int(input("Choose the process you want to:\n1. Change the required amount of money.\n2. Quit."))

                    if process3 == 2:
                        print("Have a nice day!")
                        sys.exit()


                    elif process3 == 1:
                        # check if the required money is less than ATM total money
                        while True:
                            reqmoney = int(input(f"Enter the required amount of money under {ATMTotalMoney}:"))
                            if reqmoney <= ATMTotalMoney:
                                break

                if reqmoney <= userbalance:
                    # filling output money array and changing categories values in dictionary:
                    for i in categories.keys():
                        while reqmoney >= int(i) and categories[i] > 0:
                            categories[i] -= 1
                            reqmoney -= int(i)
                            OutputMoney.append(int(i))
                    # calculating new user balance:
                    for i in OutputMoney:
                        clients[user]["balance"] -= i  # at dictionary
                        balance_array[userindex] -= i  # at balance_array
                        
                    # styling 
                    sys.stdout.write("preparing money")
                    name = ". . . . .\n"
                    for char in name:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.5)

                    print(f"Successful process! please take the money and your card!\n\nYour money categories will be as follows: {OutputMoney}")

                    # apologize if the 5 pounds category doesn't exist
                    n = len(str(reqmoney))
                    if (str(reqmoney)[n - 1] == "5" or str(reqmoney)[n - 1] == "6" or str(reqmoney)[n - 1] == "7" or str(reqmoney)[n - 1] == "8" or str(reqmoney)[n - 1] == "9") and categories["5"] == 0:
                        print("\nSorry for non-existence of some money categories.\nnote that your balance didn't get reduced by its values.")

                    # printing the new balance:
                    print(f"\nYour new balance is: {balance_array[userindex]}, have a nice day!")
                    # adding the new values of clients to json file:
                    f = open('data.json', "w")
                    f.write(json.dumps(clients, indent=3))
                    f.close()
                    # adding the new values of categories to json file:
                    f = open('moneycategory.json', 'w')
                    f.write(json.dumps(categories, indent=3))
                    f.close()
                    sys.exit()
    elif process == 2:

        # check if the required money is less than 5k EGP:
        while True:
            reqmoney = int(input("Enter the amount of money, maximum 5,000 EGP:"))
            if reqmoney <= 5000:
                break

        if reqmoney <= 5000:
            if reqmoney > userbalance:
                print(f"You have only {userbalance}, Re-Enter the required amount of money:")
                reqmoney = int(input())
            # check if the required money is less than ATM total balance:
            if reqmoney > ATMTotalMoney:
                print(f"Sorry there is no enough money at the moment.\nThere is only {ATMTotalMoney}, would you like to change the required amount of money?")
                process3 = int(input("Choose the process you want to:\n1. Change the required amount of money.\n2. Quit."))

                if process3 == 2:
                    print("Have a nice day!")
                    sys.exit()


                elif process3 == 1:
                    # check if the required money is less than ATM total money
                    while True:
                        reqmoney = int(input(f"Enter the required amount of money under {ATMTotalMoney}:"))
                        if reqmoney <= ATMTotalMoney:
                            break

            if reqmoney <= userbalance:
                # filling output money array and changing categories values in dictionary:
                for i in categories.keys():
                    while reqmoney >= int(i) and categories[i] > 0:
                        categories[i] -= 1
                        reqmoney -= int(i)
                        OutputMoney.append(int(i))
                # calculating new user balance:
                for i in OutputMoney:
                    clients[user]["balance"] -= i  # at dictionary
                    balance_array[userindex] -= i  # at balance_array

                # styling xd
                sys.stdout.write("preparing money")
                name = ". . . . .\n"
                for char in name:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.5)

                print(f"Successful process! please take the money and your card!\n\nYour money categories will be as follows: {OutputMoney}")

                # apologize if the 5 pounds category doesn't exist
                n = len(str(reqmoney))
                if (str(reqmoney)[n - 1] == "5" or str(reqmoney)[n - 1] == "6" or str(reqmoney)[n - 1] == "7" or str(reqmoney)[n - 1] == "8" or str(reqmoney)[n - 1] == "9") and categories["5"] == 0:
                    print("\nSorry for non-existence of some money categories.\nnote that your balance didn't get reduced by its values.")

                # printing the new balance:
                print(f"\nYour new balance is: {balance_array[userindex]}, have a nice day!")
                # adding the new values of clients to json file:
                f = open('data.json', "w")
                f.write(json.dumps(clients, indent=3))
                f.close()
                # adding the new values of categories to json file:
                f = open('moneycategory.json', 'w')
                f.write(json.dumps(categories, indent=3))
                f.close()
                sys.exit()