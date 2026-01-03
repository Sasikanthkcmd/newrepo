def even_odd(x):
    if x%2==0:
        return 0
    else:
        return 1
n=int(input("enter the number"))
s=even_odd(n)
if s==0:
    print("even")
else:
    print("odd")

