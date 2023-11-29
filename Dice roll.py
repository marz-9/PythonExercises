def countInput(n):
    
    counter=[]
    for i in range(1, n+1):
        attempts=input("Enter our attempts: ").split(",")
        counter.append(attempts.count(str(i)))
    return counter

def printCount(lst):
    for j in range(1, len(lst)+1):
        print("{}: {}".format(j,lst[j-1]))

def main():
    sides=int(input("Enter the number of sides for the dice: "))
    count_list=countInput(sides)
    printCount(count_list)

main()