#map is a higher order function that applies a given function to each element in iterable it repturns the map object
'''n=[1,2,3,4,5]
def square(x):
    return x*x
result=list(map(square,n))
print(result)'''#[1, 4, 9, 16, 25]
'''n=[1,2,3,4,5]
s=list(map(lambda x:x*x,n))
print(s)'''# [1, 4, 9, 16, 25]
'''n=[1,2,3,4,5]
h=list(map(lambda x:x*2,n))
print(h)'''#[2, 4, 6, 8, 10]
'''s=["1","2","3","4","5"]
h=list(map(lambda x:int(x),s))
print(h)'''#converting string to int#[2, 4, 6, 8, 10]
'''s1=[1,2,3,4,5]
s2=[3,4,5,6,7]
s=list(map(lambda x,y:x+y,s1,s2))
print(s)'''#[4,6,8,10,12] add two lists




