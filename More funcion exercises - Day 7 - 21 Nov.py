#area of polygon
"""from math import *
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
print("The area of a polygon is: ", round(result,2))"""

#count vowels
v="aoeui"
counter = 0
message=input("Enter a text:" )
def vowelcounter(stri):
    for chr1 in stri:
        if(chr1 in v):
            stri1 +=chr1.upper()
        stri2= stri.replace(stri, stri1)
    return stri2
print(vowelcounter(message))


   
    