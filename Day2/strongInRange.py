#to print strong numbers within range 1-N
def fact(n):
    if(n==0 or n==1):
        return 1
    f=1
    i=1
    while(i<=n):
        f*=i
        i+=1
    return f
def strong(n):
    for i in range(1,n):
        temp=i
        sum=0
        while(i>0):
            r=i%10
            sum=sum+fact(r)
            i//=10
        if(temp==sum):
            print(temp,end=" ")

num=int(input("Enter N value : "))
print("Strong numbers between 1-",num)
strong(num)
    