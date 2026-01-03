def prime():
    n=int(input("entre the number"))
    i=2
    found=0
    while(i<n):
        if n%i==0:
            print(f"{n} is not a prime")
        i=i+1
    print(f"{n} is  a prime")
prime()
