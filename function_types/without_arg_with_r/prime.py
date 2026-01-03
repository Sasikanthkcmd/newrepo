def prime():
    x=int(input("entre the number"))
    i=2
    found=0
    while(i<x):
        if x%i==0:
            found=1
        i=i+1
    return found
s=prime()
if s==0:
    print(" given number prime")
else:
     print(" given number  is not a prime")

