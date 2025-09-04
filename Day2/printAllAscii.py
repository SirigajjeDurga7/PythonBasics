#to print all ascii characters
def printAscii():
    for i in range(0,256):
        print(f"{i}--->{chr(i)}")

print("All Ascii characters with values:\nValue--->Ascii character")
printAscii()
    