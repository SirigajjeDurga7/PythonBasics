#palindromes in given range 1-N
def reverse(m):
    rev=0
    while(m>0):
        r=m%10
        rev=rev*10+r
        m=m//10
    return rev

def palin(n):
    for i in range(1,n):
        rev=reverse(i)
        if(i==rev):
            print(i,end=" ")

num=int(input("Enter N value : "))
palin(num)