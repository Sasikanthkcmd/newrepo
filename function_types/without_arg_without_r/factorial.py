def fact_num():
    n=int(input("enter the number"))
    i=1
    res=1
    while(i<=n):
        res=res*i
        i+=1
    print(f"fact of {n} is {res}")
fact_num()

