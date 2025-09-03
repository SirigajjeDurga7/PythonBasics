#to check number divisible by 5 and 11 or not
def divisibleBy5and11(n):
    if n%5==0 and n%11==0:
        print("Divisible by 5 and 11")
    else:
        print("Not divisible")
x=int(input("Enter number : "))
divisibleBy5and11(x)