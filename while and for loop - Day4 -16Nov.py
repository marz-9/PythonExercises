start=1
n=int(input("Enter a number: "))
summ=0
while(start<=n):
    summ+=start
    start+=1
print("The sum = ", summ)

#Sum of digits
i=0
n=input("Enter a number: ")
summ=0
while(i<len(n)):
    summ+=int(n[i])
    i+=1
print("The sum = ", summ)

i=0
n=int(input("Enter a number: "))
summ=0
while(i<=len(str(n))):
    summ+=n%10
    n=n//10
    i+=1
    print(n)
print("The sum = ", summ)


n=int(input("Enter a number: "))
summ=0
while(n != 0):
    summ+=n%10
    n=n//10
    print(n)
print("The sum = ", summ)

#coninue
i=0
while(i<=6):
    if(i == 4):
        i+=1
        continue
    print(i)
    i+=1

#break
i=0
while(i<=6):
    i+=1
    if(i == 4):
        break
    print(i)


#Dechiper example
message="|rx#duh#juhdwh"
x=0
while(x<len(message)):
    new=ord(message[x])-3
    print(chr(new), end="")
    x+=1
    

for i in range(1,5):
    print("*"*i)
    
for i in range(4,0,-1):
    print("*"*i)         


#Guess the number exercise
i=0
while(i == i):
    i=int(input("Enter a number: "))
    if (i == 19):
        print("Win")
        break
    elif (i < 19):
        print("Go up")
    elif (i > 19):
        print("Go Down")

    
    