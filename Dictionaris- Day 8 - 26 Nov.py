"""dictt={1:"B", 2:"C"}
#It will print X if the key is not present in dictionary
print(dictt.get(3,"X"))
#It will print the original value of key 2
print(dictt.get(2,"X"))

#Remove value in dictionary
dictt.pop(2)
print("After removing the key 2 he result is: ",dictt.values())
print()

#for loop to print dictionary values
dict_1 = {1:{"name":"Sara", "age":20}, 2:{"name":"Muna","age":22}}
for x in dict_1:
    print(dict_1[x])
print()

#for loop to print dictionary values in a nested dictionary
dict2 = {1:{"name":"Sara", "age":20}, 2:{"name":"Muna","age":22}}
for key in dict2:
    for key1 in dict2[key]:
        print(dict2[key][key1])

print()

#Print the name of people who are above 22 years old
dict3 = {1:{"name":"John", "age":27, "sex":"Male"},
         2:{"name":"Marie","age":22, "sex":"Female"},
         3:{"name":"Sali","age":23,"sex":"Female"}}
print("Peopl's name whose age is above 22 are: ")
for k1 in dict3:
    if (dict3[k1]["age"]>22):
        print(dict3[k1]["name"])

#tuples
def func1(t):
    t*=2
    print(t)
t=(1,2,3)
print(t)
func1(t)
print(t)"""
#removing element in tuple cannot be done, as tuples are immutable t.pop()


#sets
#it does accept to convert list to a set but creating a set={[1,2,4]} does not accept list
#lists are accepted only in set() function for conversion
set1=set([1,5,3,4,7,9,2,10,2,3])
print(set1)

set2=set([1,5,3,4])
#adding one value
set2.add('b')
#to add more than one
set2.update(("c",35,36))

print(set2)
