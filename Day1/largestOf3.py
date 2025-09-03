#to check greatest of 3 numbers using nested-if
def greatest(a,b,c):
    if(a>b):
        if(a>c):
            print("a is big")
        else:
            print("c is big")
    else:
        if(b>c):
            print("b is big")
        else:
            print("c is big")

x=int(input("Enter a number : "))
y=int(input("Enter b number : "))
z=int(input("Enter c number : "))
greatest(x,y,z)