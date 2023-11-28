#multipling 2 matrix
"""matrix=[[1,2,3],[6,7,8]]
matrix2=[[6,1],[2,10],[0,2]]

def multiply_matrix(m1,m2):
    matrix3=[[0,0],[0,0]]
    for row in range(len(m1)):
        for col in range(len(m2[0])):
            for row2 in range (len(m2)):
                matrix3[row][col]+=m1[row][row2]*m2[row2][col]
            
    return matrix3
print(multiply_matrix(matrix,matrix2))
print()

#reading line from a file using readline()
file = open("test.txt","r")
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
#After the last line no \n is printed/added
print(file.readline())
#reading line from a file using readline()
print("Using read fucntion:")
print(file.read())
file1 = open("test.txt","r")
line = file1.readline()
while (line != ""):
    line = file1.readline()
    print(line)
    
#calculating average from a file
file2= open("average.txt", "r")
listt=[float(i) for i in file2.read().split("\n")]
print("average= ",sum(listt)/len(listt))

#using while to calculate avg
file3= open("average.txt", "r")
line2 = file3.readline()
count=0
sum1=0
for line2 in file3:
    print(line2)
    sum1 += float(line2)
    count+=1
print(sum1/count)

#writing to a file
f = open("test.txt","w")
print("hello Python", file=f)
f.close()

input_file=open("test2.txt","r")
for line3 in input_file:
    line3=line3.rsplit(" ")
    print(line3)"""
    
input_file2=open("grades.txt","r")
for line4 in input_file2:
    line4=line4.split(" ")
    print(line4[0], "mark is: ", line4[1])    

print()

input_file2=open("grades.txt","r")
for line4 in input_file2:
    line4=line4.split(" ")
    if (int(line4[1]) > 70):
        print(line4[0], "mark is: ", line4[1])  

