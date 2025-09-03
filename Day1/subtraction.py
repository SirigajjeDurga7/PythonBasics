#fun to subtract 2 numbers with returntype, no arguments
def sub():
    a=int(input("Enter a value : "))
    b=int(input("Enter b value : "))
    c=a-b
    return c
res=sub()
print("Difference = ",res)