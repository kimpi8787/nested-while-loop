i=5
while i>=1:
    j=1
    while j<=i:
        print(j,end="")
        j=j+1
    print()
    i=i-1


##2
i=5
while i>=1:
    j=5
    while j>=i:
        print(i,end="")
        j=j-1
    print()
    i=i-1


##3
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


##4
i=1
while i<=5:
    j=1
    while j<=5:
        if j==1 or j==5 or i==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    print()
    i=i+1


##5
i=1
while i<=5:
    j=1
    while j<=5:
        if j==1 or j==2 or j==3 or i==1 or i==2 or i==4 or i==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    print()
    i=i+1

##6
i=1
l=1
while i<=4:
    k=1
    while k<=4-i:
        print(" ",end=" ")
        k=k+1
    j=1
    while j<=l:
        print("*",end=" ")
        j=j+1
    l=l+2
    print()
    i=i+1