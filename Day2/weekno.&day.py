#to print week day based on week number
def weekDay(n):
    if n==1:
        return "Sunday"
    elif n==2:
        return "Monday"
    elif n==3:
        return "Tuesaday"
    elif n==4:
        return "Wednesday"
    elif n==5:
        return "Thursday"
    elif n==6:
        return "Friday"
    elif n==7:
        return "Saturday"
    else:
        print("Invalid")

num=int(input("Enter week no. : "))
print("Week day:",weekDay(num))