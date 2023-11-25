#Question 1 Decipher Message
message="|rx#duh#juhdwh"
x=0
while(x<len(message)):
    new=ord(message[x])-3
    print(chr(new), end="")
    x+=1
    
#Question 2 Star shape
for i in range(1, 5):
    print("*" * i)

for i in range(5, 0, -1):
    print("*" * i)

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
