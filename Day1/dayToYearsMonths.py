#to convert days to years and months 
def toYearAndMonth(days):
    y=days/365
    m=days/30
    print("Years=",round(y,3))
    print("Months=",round(m,3))
day=int(input("Enter no.of days : "))
toYearAndMonth(day)