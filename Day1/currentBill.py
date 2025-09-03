#curremtBill
n=int(input("Enter consumer number : "))
name=input("Enter consumer name : ")
pre_reading=int(input("Enter present month reading : "))
last_reading=int(input("Enter last month reading : "))
totalUnits=pre_reading-last_reading
bill=totalUnits*3.80
print("DETAILS-")
print("Consumer number : ",n,"\nConsumer name : ",name)
print("Present month reading = ",pre_reading,"\nLast month reading = ",last_reading)
print(f"Total units = {totalUnits}\nBill amount = {bill}")
