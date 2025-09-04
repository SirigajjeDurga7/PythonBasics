#armstrong numbers in range 1-N
def sumOfCubes(m,c):
    sum=0
    while(m>0):
        r=m%10
        sum=r**c+sum
        m=m//10
    return sum

def armstrong(n):
    for i in range(1,n):
        temp=i
        c=0
        while(i>0):
            c+=1
            i=i//10
        rev=sumOfCubes(temp,c)
        if(temp==rev):
            print(temp,end=" ")

num=int(input("Enter N value : "))
armstrong(num)