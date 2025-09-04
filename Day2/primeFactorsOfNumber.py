#program to find all prime factors of a number.
def primeFactors(n):
    for i in range(1,n+1):
        if(n%i==0):
            c=0
            for j in range(1,i+1):
                if(i%j==0):
                    c+=1
            if(c==2):
                print(i)


num=int(input("Enter a number : "))
print("Prime factors of",num)
primeFactors(num)