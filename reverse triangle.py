n=int (input ("enter a number:"))
for i in range (n+1):
    for j in range (n-i):
        print(" ",end="")
    for j in range (i):
        print("*",end="")
    print()
