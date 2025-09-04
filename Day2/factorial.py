#to print factorial of number
def fact(n):
    if n==0 or n==1:
        return 1
    i=1
    f=1
    while(i<=n):
        f*=i
        i+=1
    return f

x=int(input("Enter number : "))
print(f"Factorial of {x} is {fact(x)}")