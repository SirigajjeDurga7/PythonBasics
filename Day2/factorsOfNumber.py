#program to find all factors of a number
def factors(n):
    for i in range(1,n+1):
        if(n%i==0):
            print(i)

num=int(input("Enter a number : "))
print("factors of",num)
factors(num)