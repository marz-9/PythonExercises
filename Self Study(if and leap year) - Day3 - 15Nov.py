#Greatest number
a=int(input("Enter number A: "))
b=int(input("Enter number B: "))
c=int(input("Enter number C: "))

if (a>b and a>c):
    print("Number A is the greatest: ", a)
elif (b>a and b>c):
    print("Number B is the greatest: ", b)
elif (c>a and c>b):
    print("Number C is the greatest: ", c)
else:
    print("Please enter unequal numbers.")

#Leap year exercise
num_year = int(input("Enter a year number: "))

if (num_year % 400 == 0) and (num_year % 100 == 0):
    print(num_year, " is a leap year")
elif (num_year % 4 ==0) and (num_year % 100 != 0):
    print(num_year, " is a leap year")
else:
    print(num_year, " is not a leap year")

