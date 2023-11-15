g=int(input("Please Enter a Number: "))

if (g%2==0):
    print("The number is even")
else:
    print("The number is odd")
    
#also if you wrote a negative number it'll still check
#if it's even or odd
    
#discount exercise
totalamount=int(input("Enter total amount of shopping cart: "))
if (totalamount>=100):
    discount=totalamount-(totalamount*10/100)
    print("Your total amount after 10% discount: "+str(discount))
else:
    discount=totalamount-(totalamount*5/100)
    print("Your total amount after 5% discount: "+str(discount))
    
#job gender and age exercise  
gender=input("Enter your gender: ")
if (gender=="male" or gender=="Male"):
    print("Gender: "+gender)
    age=int(input("Enter your age: "))
    if (age>=24 and age<=30):
        print("Final result: Accepted for the job requiremnts.")
    else:
        print("Sorry, you don't fit the age requirement.")
else:
    print("Sorry, you don't fit the requirement.")


#hour minute checking exercise
hour1=int(input("Enter the first timing: "))
minute1=int(input("Enter it's minutes: "))
ampm1=input("Enter am or pm: ")
hour2=int(input("Enter the second timing: "))
minute2=int(input("Enter it's minutes: "))
ampm2=input("Enter am or pm: ")

if (ampm1=="am" and ampm2=="pm"):
    if (0<=hour1<=12 and 0<=minute1<=59):
        print("The time that comes first: "+str(hour1)+":"+str(minute1)+" "+ampm1)
    else:
        print("Please enter time correctly.")
elif (ampm2=="am" and ampm1=="pm"):
    if (0<=hour2<=12 and 0<=minute2<=59):
        print("The time that comes first: "+str(hour2)+":"+str(minute2)+" "+ampm2)
    else:
        print("Please enter time correctly.")
else:
    if (0<=hour1<=12 and 0<=hour2<=12):
        if (hour1<=hour2):
            if(0<=minute1<=59 and 0<=minute2<=59):
                if (minute1<=minute2):
                    print("The time that comes first: "+str(hour1)+":"+str(minute1)+" "+ampm1)
                else:
                    print("Please enter time correctly.")
            else:
                print("Please enter time correctly.")
        elif (hour2<=hour1):
            if(0<=minute1<=59 and 0<=minute2<=59):   
                if (minute2<=minute1):
                    print("The time that comes first: "+str(hour2)+":"+str(minute2)+" "+ampm2)
                else:
                    print("Please enter time correctly.")
            else:
                print("Please enter time correctly.")
        else:
            print("Please enter time correctly.")


#ATM exercise.
pin=1234
balance=1000
epin=int(input("Please enter your pin: "))
if (epin==pin):
    num=int(input("""Choose the following:
                        1.Check Balance
                        2.Withdraw Money
                        3.Deposit Money
                        4.Exit
                        : """))
    if (num == 1):
        print("Your balance is: "+str(balance)+" OMR")
    elif (num == 2):
        withdraw=int(input("Enter the amount to withdraw: "))
        nbalance=balance-withdraw
        print("You withdraw: "+str(withdraw)+" OMR. Your balance is now: "+str(nbalance)+" OMR.")
    elif (num == 3):
        d_or_t=int(input("""deposite to:
                                    1.your account
                                    2.other account"""))
        #deposite in your account.
        if (d_or_t == 1):
            deposit=int(input("Enter the amount: "))
            nbalance=balance+deposit
            print("You deposit: "+str(deposit)+" OMR. Your balance is now: "+str(nbalance)+" OMR.")
        #deposit for someone else.
        else:
            deposit=int(input("Enter the amount to deposit: "))
            baccount=int(input("Enter beneficiary account: "))
            nbalance=balance-deposit
            print("You deposit: "+str(deposit)+" OMR to "+str(baccount)+". Your balance is now: "+str(nbalance)+" OMR.")
    elif (num == 4):
        print("Thank you")
    else:
        print("Please choose from the number list.")
else:
        print("Wrong PIN number")
    