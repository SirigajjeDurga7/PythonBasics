#to find sum of first and last digit of a number
def sumFirstLast(n):
    if n==0:
        print("Sum of first and last digit=0")
        return
    else:
        last=n%10
        while(n>0):
            r=n%10
            n//=10
        first=r
    print(f"First digit={first} and last digit={last}")
    print(f"Sum of first and last digit={first+last}")

num=int(input("Enter a number : "))
sumFirstLast(num)