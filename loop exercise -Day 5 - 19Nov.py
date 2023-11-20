#Question 2 Star shape

#Question 3 Perfect number
summ = 0
n=int(input("Enter a number:"))

for y in range(1,n+1):
    for i in range (1, y):
        if(y%i == 0):
            summ+=i
    if (summ == y):
        print(str(summ)+" is a perfect number")
    summ=0

#Question 4 Narcissitic number
number=int(input("Enter a number: "))

for number in range(1,number+1):
    result = 0
    for digit in str(number):
        result += (int(digit) ** 3)   
        if (result == number):
            print(number)
            print("yes")
            