n=5
r=1
for i in range(1,n+1):
    if (i !=n):
        print(i, end='*')
    else:
        print(i,"=", end="")
    r*=i
print(r)

z=1
s=1
while(z<=n):
    if (z !=n):
        print(z, end='*')
    else:
        print(z,"=", end="")
    s*=z
    z+=1
print(s)

#To use break add if condition after increment in an if condiion as in the example
c=1
y=1
while(True):
    if (c !=n):
        print(c, end='*')
    else:
        print(c,"=", end="")
    y*=c
    c+=1
    if (c == n+1):
        break
print(y)

#print number of series n term and get addition result
num=int(input("Enter a number:"))
sum1=0
for w in range(1, num+1):
    p=w*"2"
    sum1+=int(p)
    if (w !=num):
        print(p, end='+')
    else:
        print(p,"= ", end="")
print(sum1)


q_answer="abaacb"
mark = 0
answer=input("Enter answers:" )

if(len(answer)==6):
    for i in range(len(q_answer)):
        if( answer[i]==q_answer[i]):
             mark+=1
        else:
            print("Q",i+1)
    print("\nYour final result: ",mark,"/",len(q_answer)) 
else:
    print("Enter the correct number of answers.")
   
#using for loop in a function

def grade_exam(q_num,marks):
    
    q_answer=input("Enter the answer of {} questions: ".format(q_num))
    answer=input("Enter answers: " )
    for i in range(len(q_answer)):
        if( answer[i]==q_answer[i]):
            rmarks+=marks
    print("Your final result: ",rmarks, "/ ",len(q_answer)*marks)
           
grade_exam(6,2)           
           


#Function example to enter fixed number of arguments
def sum_num(a,b):
    return a+b
result = sum_num(1,2)
print(result)


#Function example to enter more than 1 argument
def sum_num(*args):
    sum3=0
    for n in args:
        sum3+=n
    return sum3

result = sum_num(1,2,4)
print(result)


#Adding a main function
def main():
    result = sum_num(1,5,4,5,-3)
    print(result)
def sum_num(*args):
    sum3=0
    for n in args:
        sum3+=n
    return sum3

main()

#Private variable (means within a function)
def main():
    print(func1(2),func2(1))
def func1(x):
    num=5
    return x*num
def func2(x):
    i=4
    y=3
    return i*x+y

main()

#Global variable in a function
num=5
def main():
    print(func1(2),func2(1))
def func1(x):
    return x*num
def func2(x):
    i=4
    y=3
    return i*x+y-num

main()


#sum of digits 
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


