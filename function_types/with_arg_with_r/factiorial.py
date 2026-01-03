def fact_num(x):
    i=1
    res=1
    while(i<=x):
        res=res*i
        i+=1
    return res    
n=int(input("enter the number"))
s=fact_num(n)
print(f"fact of num{n} is {s}")
