def main():
    
    #list1=readFloat(5)
    #print("Numbers you entered: ",list1)
    #number=int(input("Enter the factor number: "))
    #new_list1=multiply(list1,number)
    #print("After multiplying the result: ",new_list1)
    #final=printReverse(new_list1)
    #print(final)
    #To shortcut the number of lines
    number=int(input("Enter the factor number: "))
    final=printReverse(multiply(readFloat(5),number))
    print(final)
    
def readFloat(n):
    result=[]
    for i in range(n):
        values=float(input("Enter float numbers: "))
        result.append(values)
    return result

def multiply(ls,factor):
    for i in range(len(ls)):
        ls[i]=ls[i]*factor
    return ls

def printReverse(ls):
    ls.reverse()
    return ls

main()


#nested matrix
matrix= [[2,5,1],
         [4,9,0],
         [11,6,7]]

for x in range(len(matrix)):
    for y in range(len(matrix)):
        print(matrix[x][y]*2, end=" ")
    print()
    
matrix= [[0,5,1],
         [4,9,0],
         [0,6,0]]
counter=0
for x in range(len(matrix)):
    for y in range(len(matrix)):
        if (matrix[x][y] == 0):
            counter+=1
print(matrix[x][y], "->", end=" ")
print(counter)
#print(counter)


#function to add two matrix


matrix1=[[0,5,1],
         [4,9,0],
         [0,6,0]]

matrix2=[[5,5,1],
         [5,8,1],
         [9,2,6]]
    
def addmatrix(mat1,mat2):
    matrix3=[]
    for row in range(len(mat1)):
        rows=[]
        for col in range(len(mat1)):
            rows.append(mat1[row][col]+mat2[row][col])
        matrix3.append(rows)
    return matrix3
print(addmatrix(matrix1,matrix2))

#diagonal 1
num1=int(input("Enter number: "))

for k in range(num1):
    for n in range(num1):
        if (k==n):
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()

num2=int(input("Enter number: "))

for k2 in range(num2):
    for n2 in range(num2):
        if (k2<=n2):
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()
    
num3=int(input("Enter number: "))

for k3 in range(num3):
    for n3 in range(num3):
        if (k3>=n3):
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()
    
