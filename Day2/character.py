# to check character is alphabet or digit or special character
def check(x):
    if(x>='A' and x<='Z') or (x>='a' and x<='z'):
        return "Alphabet"
    elif x>='0' and x<='9':
        return "Digit"
    else:
        return "Special Charcter"
    
n=input("Enter a character : ")
print("It is a ",check(n))