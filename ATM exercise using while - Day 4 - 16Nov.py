pin=0
balance=1000
while (pin==pin):
    pin=int(input("Please enter your pin: "))
    if (pin==1234):
        num=int(input("""Choose the following:
                        1.Check Balance
                        2.Withdraw Money
                        3.Deposit Money
                        4.Exit
                        : """))
        if (num == 1):
            print("Your balance is: "+str(balance)+" OMR")
            break
        elif (num == 2):
            withdraw=int(input("Enter the amount to withdraw: "))
            nbalance=balance-withdraw
            print("You withdraw: "+str(withdraw)+" OMR. Your balance is now: "+str(nbalance)+" OMR.")
            break
        elif (num == 3):
            d_or_t=int(input("""deposite to:
                                    1.your account
                                    2.other account"""))
            #deposite in your account.
            if (d_or_t == 1):
                deposit=int(input("Enter the amount: "))
                nbalance=balance+deposit
                print("You deposit: "+str(deposit)+" OMR. Your balance is now: "+str(nbalance)+" OMR.")
                break
            #deposit for someone else.
            else:
                deposit=int(input("Enter the amount to deposit: "))
                baccount=int(input("Enter beneficiary account: "))
                nbalance=balance-deposit
                print("You deposit: "+str(deposit)+" OMR to "+str(baccount)+". Your balance is now: "+str(nbalance)+" OMR.")
                break
        elif (num == 4):
            print("Thank you")
            break
        else:
            print("Please choose from the number list.")
    else:
        print("Wrong PIN number")