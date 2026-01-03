def prime(x):
    i=2
    found=0
    while(i<x):
        if x%i==0:
            found=1
        i=i+1
    return found    
n=int(input("entre the number"))
s=prime(n)
if s==0:
    print(f" given number {n} is prime")
else:
     print(f" given number {n} is not a prime")

