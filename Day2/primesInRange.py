#to display primes within given range
def primes(n):
    for i in range(1,n+1):
        j=2
        c=0
        while(j<=(i/2)):
            if(i%j==0):
                c+=1
            j+=1
        if c==0 and i!=1:
            print(i)

num=int(input("Enter n value : "))
primes(num)