#to count number of notes in given amount
def count(m):
    c=0
    if(m>=2000):
        n=m//2000
        c=c+n
        m=m-(n*2000)
    if(m>=500):
        n=m//500
        c=c+n
        m=m-(n*500)
    if(m>=200):
        n=m//200
        c=c+n
        m=m-(n*200)
    if(m>=100):
        n=m//100
        c=c+n
        m=m-(n*100)
    if(m>=50):
        n=m//50
        c=c+n
        m=m-(n*50)
    if(m>=20):
        n=m//20
        c=c+n
        m=m-(n*20)
    if(m>=10):
        n=m//10
        c=c+n
        m=m-(n*10)
    if(m>=5):
        n=m//5
        c=c+n
        m=m-(n*5)
    if(m>=2):
        n=m//2
        c=c+n
        m=m-(n*2)
    if(m>=1):
        n=m//1
        c=c+n
        m=m-(n*1)
    return c

amount=int(input("Enter amount : "))
print("Number of notes=",count(amount))
