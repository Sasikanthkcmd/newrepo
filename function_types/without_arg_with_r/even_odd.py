def even_odd():
    x=int(input("enter the number"))
    if x%2==0:
        return 0
    else:
        return 1
s=even_odd()
if s==0:
    print("even")
else:
    print("odd")
