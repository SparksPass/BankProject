import time
import sys
import os


spinner = ["|", "/", "-", "\\"]

text = "success"

v_balanceData = [""]
v_balance = [0.00]
v_name = [""]
v_password = [""]

v_creation = ""
v_correctPassword = ""

v_newName = ""
v_newNamePass = False
v_newPassword = ""

v_inName = ""
v_inNamePass = False
v_inPassword = ""
v_inPasswordPass = False

v_account = ""
v_accountNumber = 0
v_input = ""
v_logged = False

v_noAccountData = ""
v_noAccounts = 0
v_deposit = 0.00
v_loan = 0.00
v_debtData = [""]
v_debt = [0.00]
v_pay = 0.00
v_transfer = ""
v_transferPass = False
v_transferAmount = 0.00

def new(n):
    v_balance.append(n)
    v_name.append(n)
    v_password.append(n)
    v_debt.append(n)
    return




with open("Namedata.txt", "r") as file:
    v_name = file.read().splitlines()
with open("Passworddata.txt", "r") as file:
    v_password = file.read().splitlines()
with open("Balancedata.txt", "r") as file:
    v_balanceData = file.read().splitlines()

v_balance = [float(num) for num in v_balanceData]


with open("Debtdata.txt", "r") as file:
    v_debtData = file.read().splitlines()

v_debt = [float(num) for num in v_debtData]

with open("NumberOfAccountsData.txt", "r") as file:
    v_noAccountData = file.read().strip()

v_noAccounts = int(v_noAccountData)

while True:

    v_creation = str(input("Do you have an account? :"))

    if v_creation in ["No", "no", "n", "N"]:

        v_noAccounts += 1
        new(v_noAccounts)

        v_newName = " "
        v_newNamePass = False
        v_newPassword = " "

        while len(v_newName) > 10 or len(v_newName) < 3 or v_newNamePass == False:
            v_newName = str(input("Enter your username :"))
            if len(v_newName) > 10 or len(v_newName) < 3:
                print ("Error, username must be 3 to 10 characters long")
            else:
                if v_newName in v_name:
                    print ("Error, username taken")
                else:
                    v_newNamePass = True

        while len(v_newPassword) != 8:
            v_newPassword = str(input("Enter 8-character password :"))
            if len(v_newPassword) != 8:
                print ("Error, password must be 8 characters")

        print("Press enter to confirm :")
        input()

        for _ in range(10):
            for frame in spinner:
                sys.stdout.write(f"\rLoading {frame}")
                sys.stdout.flush()
                time.sleep(0.05)
        print("\nDone!")



        with open("Namedata.txt", "a") as file:
            file.write(v_newName + "\n")
        with open("Passworddata.txt", "a") as file:
            file.write(v_newPassword + "\n")
        with open("Balancedata.txt", "a") as file:
            file.write(str(0.00) + "\n")
        with open("Debtdata.txt", "a") as file:
            file.write(str(0.00) + "\n")
        with open("NumberOfAccountsData.txt", "w") as file:
            file.write(str(v_noAccounts))

        with open("Namedata.txt", "r") as file:
            v_name = file.read().splitlines()
        with open("Passworddata.txt", "r") as file:
            v_password = file.read().splitlines()
        with open("Balancedata.txt", "r") as file:
            v_balanceData = file.read().splitlines()
        v_balance = [float(num) for num in v_balanceData]
        with open("Debtdata.txt", "r") as file:
            v_debtData = file.read().splitlines()
        v_debt = [float(num) for num in v_balanceData]
        with open("NumberOfAccountsData.txt", "r") as file:
            v_noAccountData = file.read().strip()
        v_noAccounts = int(v_noAccountData)

    elif v_creation in ["Yes", "yes", "y", "Y"]:

        v_inName = " "
        v_inNamePass = False
        v_inPassword = " "
        v_inPasswordPass = False
        v_correctPassword = " "

        while len(v_inName) > 10 or len(v_inName) < 3 or v_inNamePass == False:
            v_inName = str(input("Enter your username :"))
            if len(v_inName) > 10 or len(v_inName) < 3:
                print("Error, username must be 3 to 10 characters long")
            else:
                if not v_inName in v_name:
                    print ("Error, user not found")
                else:
                    v_inNamePass = True

        while len(v_inPassword) != 8 or v_inPasswordPass == False:
            v_inPassword = str(input("Enter 8-character password :"))
            if len(v_inPassword) != 8:
                print ("Error, password must be 8 characters")
            else:
                v_correctPassword = v_password[v_name.index(v_inName)]
                if v_inPassword == v_correctPassword:
                    v_inPasswordPass = True
                else:
                    print ("Error, wrong password")

        print ("Press enter to confirm :")
        input()

        for _ in range(10):
            for frame in spinner:
                sys.stdout.write(f"\rLoading {frame}")
                sys.stdout.flush()
                time.sleep(0.05)
        print("\nDone!")


        v_account = v_inName
        v_logged = True
        v_accountNumber = [v_name.index(v_account)]

        print(f"logged into {v_inName}")
        print("Type /help for all commands")

        while v_logged == True:
            v_input = " "
            v_input = str(input())

            if v_input == "/help":
                print ("/help - Shows all command")
                print ("/logout - Logs out of the account")
                print ("/info - Shows account information")
                print ("/deposit - Add money to account")
                print ("/loan - Get a loan")
                print ("/pay - Pay off loans")
                print ("/transfer - Transfer money to another account")

            if v_input == "/logout":
                for _ in range(10):
                    for frame in spinner:
                        sys.stdout.write(f"\rLoading {frame}")
                        sys.stdout.flush()
                        time.sleep(0.05)
                print("\nDone!")
                v_logged = False

            if v_input == "/info":

                print (f"Username : {v_account}")
                print (f"Password : {v_inPassword}")
                print (f"Balance : £{v_balance[v_name.index(v_account)]}")
                print (f"Debt : £{v_debt[v_name.index(v_account)]}")

            if v_input == "/deposit":
                v_deposit = 0.00
                while v_deposit <= 0:
                    v_deposit = float(input("Enter amount of money to deposit :"))
                    if v_deposit <= 0:
                        print ("Error, deposit must be above £0")
                print ("Press enter to confirm :")
                input()
                v_balance[v_name.index(v_account)] += v_deposit
                with open("Balancedata.txt", "w") as file:
                    for value in v_balance:
                        file.write(f"{value}\n")

                print("\nDone!")

            if v_input == "/loan":
                v_loan = 0.00
                while v_loan < 25 or v_loan > 2500:
                    v_loan = float(input("Enter amount of money to loan :"))
                    if v_loan < 25 or v_loan > 2500:
                        print ("Error, loan must be between £25 to £2500")
                print("Press enter to confirm :")
                input()
                v_balance[v_name.index(v_account)] += v_loan
                v_debt[v_name.index(v_account)] += v_loan
                with open("Balancedata.txt", "w") as file:
                    for value in v_balance:
                        file.write(f"{value}\n")
                with open("Debtdata.txt", "w") as file:
                    for value in v_debt:
                        file.write(f"{value}\n")

                print("\nDone!")

            if v_input == "/pay":
                if v_debt[v_name.index(v_account)] != 0:
                    v_pay = 0.00
                    while v_pay <= 0 or v_pay > v_debt[v_name.index(v_account)]:
                        v_pay = float(input("Enter amount to pay :"))
                        if v_pay <= 0:
                            print ("Error, must select amount")
                        else:
                            if v_pay > v_debt[v_name.index(v_account)]:
                                print ("Error, amount selected is too much")
                    print("Press enter to confirm :")
                    input()
                    v_debt[v_name.index(v_account)] -= v_pay
                    with open("Debtdata.txt", "w") as file:
                        for value in v_debt:
                            file.write(f"{value}\n")


                    print("\nDone!")
                else:
                    print ("Error, No loan to pay")

            if v_input == "/transfer":
                if v_balance[v_name.index(v_account)] != 0:
                    v_transferPass = False
                    v_transfer = " "
                    v_transferAmount = 0.00
                    while v_transferPass == False:
                        v_transfer = str(input("Enter account to transfer :"))
                        if not v_transfer in v_name or v_transfer == v_account:
                            print ("Error, account not found")
                        else:
                            v_transferPass = True
                    while v_transferAmount <= 0 or v_transferAmount > v_balance[v_name.index(v_account)]:
                        v_transferAmount = float(input("Enter amount to transfer :"))
                        if v_transferAmount <= 0:
                            print ("Error")
                        else:
                            if v_transferAmount > v_balance[v_name.index(v_account)]:
                                print ("Error, too much money selected")
                    print("Press enter to confirm :")
                    input()
                    v_balance[v_name.index(v_account)] -= v_transferAmount
                    v_balance[v_name.index(v_transfer)] += v_transferAmount
                    with open("Balancedata.txt", "w") as file:
                        for value in v_balance:
                            file.write(f"{value}\n")

                    print("\nDone!")
                else:
                    print ("Error, no money to transfer")







