#to generate current bill based on units
def bill(n):
    if n>=1 and n<=50:
        return 3.80
    elif n>=51 and n<=100:
        return 50*3.80+(n-50)*4.20
    elif n>=101 and n<=200:
        return 50*3.80+50*4.20+(n-100)*5.10
    elif n>=201 and n<=300:
        return 50*3.80+50*4.20+100*5.10+(n-200)*6.30
    else:
        return 50*3.80+50*4.20+100*5.10+100*6.30+(n-300)*7.50
    
n=int(input("Enter consumer number : "))
name=input("Enter consumer name : ")
pre_reading=int(input("Enter present month reading : "))
last_reading=int(input("Enter last month reading : "))
totalUnits=pre_reading-last_reading
b=bill(totalUnits)
print("DETAILS-")
print("Consumer number : ",n,"\nConsumer name : ",name)
print("Present month reading = ",pre_reading,"\nLast month reading = ",last_reading)
print(f"Total units = {totalUnits}\nBill amount = {b}")