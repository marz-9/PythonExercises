#printing the index
"""list_= [1,2,3,4]
for i in range(len(list_)):
    print(i, end=" ")
print()
    
#printing the values
for j in range(len(list_)):
    print(list_[j], end=" ")
print()

#Printing the values by using the variable only without using index
for y in list_:
    print(y, end=" ")
print()

#printing a list
for m in [2,5]:
    print(m, end=" ")


#Split a string
r="a b c"
l1=r.split(" ")
print(l1)


#copying lists and changing the value in original without affecting the second
s = [1,2,3,4,5]
x= s.copy()
print(x)
x[4]= 7
print(x)
print(s)


li2= [1, 2, 3]
for i in li2:
    print(i, end= " ")
print()

li3= [1, 2, 3]
for q in li3:
    print(q*2, end= " ")

counter2=0
li4= [1, 2, 3, -4, -5]
for u in li4:
    if (u < 0):
        counter2+=1
print(counter2)


#list functions
li5=[-2,5,-5,1,7]
print(li5)
li5.append(9)
print(li5)
li5.insert(0,1)
print(li5)
li5.pop()
print(li5)
li5.remove(7)
print(li5)
li6=[10,12]
li7=li5+li6
print(li7)

lis_result=[]
while(True):
    numlis=input("Enter numbers, when you're done enter Q: ")
    if (numlis != "Q"):
        lis_result+=numlis
    else:
        break
print(lis_result)

#position of the first number greater than 100
li_x=[100,201,99,101]
for k in li_x:
    if (k > 100):
        print(k, li_x.index(k))
        break"""


#exercise
sides_number=input("Enter the dice side: ")


def countInput(sides):
    count= sides
    
    
    
  