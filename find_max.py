#max among two numbers

def findMax(x,y):
    if(x>y):
        return x
    else:
        return y

def findMin(x, y):
    if (x < y):
        return x
    else:
        return y

a=int(input("enter the first number "))
b=int(input("enter the second number "))
if (a == b):
    print("Both =")
else:
    print("Maximum value",findMax(a,b))
    print("Minimum value",findMin(a,b))
