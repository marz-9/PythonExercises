#zeroerror and not define
try:
    x=4/0
    print(y)
except ZeroDivisionError:
    print("can not divide by zero")

#Index error
try:
    x=[1,2,3]
    print(x[3])
except Exception as exc:
    print("error: ",type(exc),str(exc))

#Value error
try:
    n=float(input("Enter a value: "))
    print(int(n))
except Exception as exc1:
    print("error: ",type(exc1),str(exc1))
    
#IOError
try:
    file1 = open("test","r")
    line = file1.readline()
    while (line != ""):
        line = file1.readline()
        print(line)
except IOError as exc2:
    print("Error: ",str(exc2))
except Exception as exc3:
    print("error: ",type(exc3),str(exc3))
finally:
    print("Done")