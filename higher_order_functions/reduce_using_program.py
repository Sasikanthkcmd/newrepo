#reduce() is a higher order function that applies a function cumulatively to the elements of an iterable and returns a single value.
from functools import reduce
'''l=[1,2,3,4,5]
s=reduce(lambda x,y:x+y,l)
print(s)'''#sum of all list elements#15
'''l=[1,2,3,4,5]
s=reduce(lambda x,y:x*y,l)
print(s)'''#product of all list elements#120
'''f=[1,7,3,9,6,4]
s=reduce(lambda x,y:x if x>y else y,f)
print(s)'''#max of numbers in list#9
'''words = ["Python", "is", "easy"]
result = reduce(lambda x, y: x + " " + y, words)
print(result)'''#join string#Python is easy




