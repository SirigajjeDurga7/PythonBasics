
def pattern(n,m):
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i==j or i+j-1==m:
                print("$",end=" ")
            else:
             print("*",end=" ")
        print()

r=int(input("Enter no.of rows: "))
c=int(input("Enter no.of columns : "))
pattern(r,c)