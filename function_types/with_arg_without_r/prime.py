def prime(x):
    i=2
    found=0
    while(i<x):
        if x%i==0:
            found=1
        i=i+1
    if found==0:
         print(f"given number {x} is prime")
    else:
        print(f"given number {x} is not a prime")
n=int(input("entre the number"))
prime(n)




