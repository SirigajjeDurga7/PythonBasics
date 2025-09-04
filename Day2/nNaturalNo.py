#to display n natural numbers
def printNum(n):
    i=1
    while(i<=n):
        print(i,end=" ")
        i+=1
num=int(input("Enter number : "))
print(num,"Natural numbers:")
printNum(num)