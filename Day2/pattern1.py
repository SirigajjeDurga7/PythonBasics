
def pattern(n,m):
    for i in range(0,n):
        for j in range(0,m):
            print("*",end=" ")
        print()

r=int(input("Enter no.of rows: "))
c=int(input("Enter no.of columns : "))
pattern(r,c)