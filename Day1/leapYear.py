#to check whether year is leap year or not
def leapOrNot(x):
    if x%4==0 and (x%400==0 or x%100!=0):
        print("leap year")
    else:
        print("Not a leap year")

year=int(input("Enter year : "))
leapOrNot(year)