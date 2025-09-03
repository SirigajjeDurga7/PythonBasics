#to check number is positive or negative
def posOrNeg(x):
    if(x>0):
        print("Positive number")
    elif x==0:
        print("Neither positive nor negative")
    else:
        print("Negative number")
n=int(input("Enter number : "))
posOrNeg(n)