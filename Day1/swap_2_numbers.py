#to swap 2 numbers
a=int(input("Enter value of a : "))
b=int(input("Enter value of b : "))
print("Before swapping a=",a,"b=",b)
#a,b=b,a
a=a+b
b=a-b
a=a-b
print("After swapping a=",a,"b=",b)