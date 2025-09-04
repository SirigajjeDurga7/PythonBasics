#to find first and last digit of a number
def firstLast(n):
    if n==0:
        first=0
        last=0
    else:
        last=n%10
        while(n>0):
            r=n%10
            n//=10
        first=r
    print(f"First digit={first} and last digit={last}")

num=int(input("Enter a number : "))
firstLast(num)
