#to print sum of n natural numbers
def sum(n):
    i=1
    sum=0
    while(i<=n):
        sum+=i
        i+=1
    return sum

num=int(input("Enter N value : "))
print(f"Sum of {num} natural numbers is {sum(num)}")