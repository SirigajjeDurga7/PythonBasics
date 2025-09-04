#program to print Fibonacci series up to n terms
def fibo(n):
    if n==0:
        print("0")
    elif n==1:
        print("0 1")
    else:
        a=0
        b=1
        print(f"{a} {b}",end=" ")
        i=1
        while(i<=n-2):
            c=a+b
            print(c,end=" ")
            a=b
            b=c
            i+=1

num=int(input("Enter N value : "))
print("Fibonacci Series-")
fibo(num)