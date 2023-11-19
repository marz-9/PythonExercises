s= "hello"
for i in range(len(s)):
    print(i, end="")
print()

s= "hello"
for i in s:
    print(i, end="")
    
v="aoeui"
counter = 0
message=input("Enter a text:" )
for chr1 in message:
    if(chr1 in v):
        counter+=1
print(counter)

#if an input was in Upper case convert to lower
# to match the v.
v="aoeui"
counter = 0
message=input("Enter a text:" )
for chr1 in message:
    if(chr1.lower() in v):
        counter+=1
print(counter)

#Count the numbers within the text
n= "0123456789"
counter = 0
message=input("Enter a text with numbers:" )
for num1 in message:
    if(num1 in n):
        counter+=1
print(counter)


#Checking the format of phone number
 
    if (len(pn)==11):
        if (pn[:3] == o):
            if (pn[3: ].isdigit()):
                pn2= pn[3:7]
                pn3= pn[7:]
                print("Your phone number is: +(",
                
                o,")",pn2,"-",pn3)
                break
            else:
                print("Please do not include characters.")
        else:
            print("Please enter the right country number.")
    else:
        print("Enter valid number length similar as the example.")  

#random library
import random
x = random.randint
print(x)

#Guess the number exercise
r= random.randint(1,20)
while(True):
    n=int(input("Enter a number: "))
    if (r == n):
        print("Win")
        break
    elif (n < r):
        print("Go up")
    elif (n > r):
        print("Go Down")
        

#Average of students grade
summ=0
stu=int(input("Enter the number of the students: "))
for i in range (1, stu+1):
    grade=float(input("Enter th students grade: "))
    summ+=grade
avg=summ/stu
print("The average grade: ",avg)

#Enter students grade based on yes or no it'll calculate the average
summ=0
i=1
while(True):
    stop=input("Enter the student grade, yes stop or no continue? (y,n)")
    if (stop.lower() == "n"):
        grade=float(input("Enter th students grade: "))
        summ+=grade
        avg=summ/i
        i+=1
        continue
    else:
        print("The average grade: ",avg)
        break

#Function to calculate the average of students grade

def grade_avg(x):
    sum2=0
    for y in range(1, x+1):
        grade=float(input("Enter the grade: "))
        sum2+=grade
    average=sum2/x
    print(average)
    
grade_avg(2)

#Function to calculate the average of students grade
stu=int(input("Enter number of students: "))
def grade_avg(x):
    sum2=0
    for y in range(1, x+1):
        grade=float(input("Enter the grade: "))
        sum2+=grade
    average=sum2/x
    print(average)
    
grade_avg(stu)

#Function to return whether it's an even number or not (Not Return example)
num = int(input("Enter a number to check if it's even or odd: "))
def check_type(number):
    if (number%2 == 0):
        print("Even")
    else:
        print("Odd")
check_type(num)

#(A Return example) Function to return whether it's an even number or not
num = int(input("Enter a number to check if it's even or odd: "))
def check_type(number):
    if (number%2 == 0):
        return "Even"
    else:
        return "Odd"

n= check_type(num)
print(n)

## or print(check_type(num))


# Functions to calculate shapes, in a loop until quit

while(True):
    choose=int(input("""Choose from the following to calculate:
                        1. Triangle
                        2. Square
                        3. Circle
                        4. Cylinder
                        5. Quit
                        """))
    if (choose == 1):
        t=0
        def triangle_cal(t):
            tbase=float(input("Enter the base of triangle: "))
            theight=float(input("Enter the height of triangle: "))
            t=(tbase*theight)/2
            return t
        result1 = triangle_cal(t)
        print("The area of triangle: ",result1)
        
    elif (choose == 2):
        s=0
        def square_cal(s): 
            swidth=float(input("Enter the width of square: "))
            slen=float(input("Enter the length of square: "))
            s=swidth*slen
            return s
        result2=square_cal(s)
        print("The area of square: ",result2)
        
    elif (choose == 3):
        c=0
        def circle_cal(c):
            r=float(input("Enter the raduis of the circle: "))
            c=3.14*(r**2)
            return c
        result3=circle_cal(c)
        print("The area of circle: ",result3)
        
    elif (choose == 4):
        cy=0
        def cylinder_cal(cy):
            cr=float(input("Enter the raduis of the cylinder: "))
            h=float(input("Enter the raduis of the cylinder: "))
            cy=(2*3.14*(cr**2))+(2*3.14*cr*h)
            return cy
        result4=cylinder_cal(cy)
        print("The area of circle: ",result4)
        
    elif (choose == 5):
        break
        
    else:
        print("Please choose from the list only.")


