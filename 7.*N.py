i=1
while i<=5:
    j=1
    while j<=5:
        if j==1 or j==i or j==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    print()
    i=i+1