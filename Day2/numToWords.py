#to convert number to words
def numToWord(n):
    reverse=0
    while(n>0):
        r=n%10
        reverse=reverse*10+r
        n//=10
    while(reverse>0):
        r=reverse%10
        if r==1:
            print("One",end=" ")
        elif r==2:
            print("Two",end=" ")
        elif r==3:
            print("Three",end="")
        elif r==4:
            print("Four",end=" ")
        elif r==5:
            print("Five",end=" ")
        elif r==6:
            print("Six",end=" ")
        elif r==7:
            print("Seven",end=" ")
        elif r==8:
            print("Eight",end=" ")
        elif r==9:
            print("nine",end=" ")
        elif r==0:
            print("zero",end=" ")
        reverse//=10

num=int(input("Enter a number : "))
numToWord(num)