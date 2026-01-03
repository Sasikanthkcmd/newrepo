def fact_num(x):
    i=1
    res=1
    while(i<=x):
        res=res*i
        i+=1
    print(f"factoril of {x} is {res}")
n=int(input("enter the number"))
fact_num(n)

