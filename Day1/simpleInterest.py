#simple Intrest and total Amount
p=int(input("Enter principal amount : "))
t=int(input("Enter time : "))
r=int(input("Enter rate of intrest : "))
simpleIntrest=(p*t*r)/100
print("Simple Intrest=",simpleIntrest)
totalAmount=simpleIntrest+p
print("Total Amount=",totalAmount)