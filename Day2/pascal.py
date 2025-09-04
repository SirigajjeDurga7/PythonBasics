#to print pascal traingle
def pascal(n,m):
    for i in range(1,n+1):
        for j in range(1,m+1):
            if(j<=m//2):
                print(" ",end=" ")
            