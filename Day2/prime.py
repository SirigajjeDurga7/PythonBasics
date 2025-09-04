#to check given number is prime or not
def prime(n):
    i=2
    while(i<=(n/2)):
        if(n%i==0):
            print("Not a prime number")
            return 
        i+=1
    print("prime number")

num=int(input("Enter number : "))
prime(num)
