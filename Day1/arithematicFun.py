#arithematic operations using functions
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return round(a/b,3)
def mod(a,b):
    return a%b

x=int(input("Enter x value : "))
y=int(input("Enter y value : "))
print("Sum=",add(x,y))
print("Difference=",sub(x,y))
print("Product=",mul(x,y))
print("Quotient=",div(x,y))
print("Remainder=",mod(x,y))