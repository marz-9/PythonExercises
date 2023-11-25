#Question 1
values=[0,0,0,0,0,0,0]
print("The values before adding ten: ",values)
values[0]=10
values[6]=10
print("The values after adding ten: ",values)

print()

#Question 2
number=[6,3,8,1,7]
print("The list before reversing: ",number)
new_num=number[::-1]
print("The list after reversing without using reverse function: ",new_num)

print()

#Question 3
colors=["red","yellow","pink","black"]
colors.insert(1,"purple")
colors.pop(3)
colors.pop(3)
colors.append("Black")
colors.append("green")
print("Question 3 output: ",colors)

print()

#Question 4
fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]
fruits.count("apple")
fruits.count("strawberry")
fruits.index("banana")
fruits.index("banana", 4)
fruits.reverse()
fruits.append("grape")
fruits.sort()
#removes last value in the list
fruits.pop()
print(fruits)

print()

#Question 5
num=[23,54,76,12,90]
for i in range (len(num)):
    if (i != 4):
        print(num[i], end="|")
    else:
        print(num[i], end="")

print()
print()

#Question 6
num2= "0"
counter = 0
message=input("Enter a text with numbers:" )
for j in message:
    if(j in num2):
        counter+=1
print(counter)

print()

#Question 7
d = "a*hj"
print(list(d))

print()

#Question 8
b= ["p", "r", "a", "c", "t", "i", "c", "e"]
for k in b:
    print(k, end="?")

print()
print()

#Question 9
c = "Hello World"
a = list(c)
print(a)
print(len(a))
print(a[1:11])
print(a[-2:-5:-1])
print(a[::2])
print(a[:4])
print(a[4:])

print()
print()

#Question 10
words=["Hello", "my", "favourite", "color", "is","Yellow"]
w=[]
while(True):
    n=input("Enter a list of words, once done type 'Q': ")
    w.append(n)
    if (n == "Q"):
        w.pop()
        if(len(w) > len(words)):
            print("The list of words entered is longer than the given list")
            print(w)
            print(words)
            break
        else:
            print("The list of words entered is not longer than the given list")
            print(w)
            print(words)
            break
