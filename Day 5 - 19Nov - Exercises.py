summ = 0
n=int(input("Enter a number:"))
#for n in range (1, 101):
for i in range (1, n):
    if(n%i == 0):
        summ+=i
if (summ == n):
    print(str(summ)+" is a perfect number")
else:
    print(str(summ)+" is not a perfect number")
        