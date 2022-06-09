i=1
while i<=5:
    j=1
    while j<=5:
        if   i==1 or j==3 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    print()
    i=i+1