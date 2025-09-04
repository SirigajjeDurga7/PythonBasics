#to count number of digits of given number
def countOfDigits(n):
    c=0
    while(n>0):
        c+=1
        n=n//10
    return c

num=int(input("Enter number : "))
print(f"Number of digits in {num} is {countOfDigits(num)}")