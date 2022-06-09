a=int(input("enter number"))
r=1
while r<=a:
    c=1
    while c<=r:
        print(" ",end="")
        c=c+1
    k=a
    while r<=k:
        print("*",end=" ")
        k=k-1
    print()
    r=r+2      

