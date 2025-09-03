#to check vowel or consonent
def check(x):
    if x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
        print("Vowel")
    else:
        print("consonent")
alpha=input("Enter a alphabet : ")
check(alpha)