#to print all perfect numbers within range 1-N
def perfect(n):
    for i in range(1,n):
        sum=0
        for j in range(1,i):
            if(i%j==0):
                sum+=j
        if(sum==i):
            print(i)

num=int(input("Enter N value : "))
print("Perfect numbers between 1-",num)
perfect(num)