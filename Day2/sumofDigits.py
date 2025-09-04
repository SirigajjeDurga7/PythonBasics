#to print sum of digits of given number
def sumOfDigits(n):
    sum=0
    while(n>0):
        sum+=n%10
        n=n//10
    return sum

num=int(input("Enter number : "))
print(f"Sum of digist of {num} is {sumOfDigits(num)}")