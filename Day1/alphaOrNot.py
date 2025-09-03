#tocheck character is alphabet or not
def alphaOrNot(x):
    num=ord(x)
    if(num>=65 and num<=90) or (num>=97 and num<=122):
        print("Alphabet")
    else:
        print("Not a Alphabet")
n=input("Enter character : ")
alphaOrNot(n)