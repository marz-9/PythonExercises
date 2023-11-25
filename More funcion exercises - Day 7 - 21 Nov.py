#Sum of digits
n=int(input("Enter a number: "))
def sum_digits(x):  
    i=x
    sum4=0
    while(i != 0):
        sum4+=i%10
        i=i//10
    return sum4
result7=sum_digits(n)
print(result7)

#area of polygon
from math import *
a=0
n=int(input("Enter the number of sides: "))
side=float(input("Enter the side: "))
def p_area(n, side):
    #n=int(input("Enter the number of sides: "))
    #side=float(input("Enter the side: "))
    a=(n*(side**2))/(4*tan(3.14/n))
    return a

result = p_area(n, side)
print("The area of a polygon is: ", result)
print("The area of a polygon is: ", round(result,2))

#Counting vowels letters and their variants in uppercase
v="aoeui"
counter = 0
message=input("Enter a text:" )
for chr1 in message:
    if(chr1.lower() in v):
        counter+=1
print(counter)

#count vowels and printing it capital
v="aoeui"
message=input("Enter a text:" )
def vowelcounter(stri):
    for old in stri:
        if(old in v):
            print(message.replace(old,old.upper()))
        
vowelcounter(message)


   
    
