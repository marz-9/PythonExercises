#Question 1 Answer

rock=int(input("Enter rock hardness value: "))
carbon=float(input("Enter carbon content value: "))
tensile=int(input("Enter tensile strength value: "))

if (rock > 50 and carbon > 0.7 and tensile > 5600):
    print("Satisfied: Grade 10")
elif (rock > 50 and carbon > 0.7):
    print("Satisfied: Grade 9")
elif (carbon > 0.7 and tensile > 5600):
    print("Satisfied: Grade 8")
elif (rock > 50 and tensile > 5600):
    print("Satisfied: Grade 7")
else:
    print("Grade 0")


#Question 2 Answer

tuition = 10000
year = 1
totalcost=0
while (year <= 14):
    year += 1
    tuition += (tuition * 5/100)
    total = round(tuition, 3)
    if (year == 10):
        print("The tuition fee in ten year is: $", total)
    if (year > 10):
        totalcost+=total     

print("The tuition fee after ten years: $", totalcost)


#Question 3 Answer

n = int(input("Enter number of rows: "))

for x in range(n):
    i=0
    for y in range(x, n):
        print("   ", end=" ")
    for y in range (x):
        print(format(2**i), end="   ")
        i+=1
    for y in range (x+1):
        print(format(2**i), end="   ")
        i-=1
    print()
