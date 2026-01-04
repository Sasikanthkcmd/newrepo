'''s={1,2,3,4,5}
s.add(6)#add one element in that time using add method
print(s)
s.update([7,0,8,9])#insert number of elements in that time using no of elements
print(s)
s.remove(3)#element is present in this list remove incase elemnt is not present in that time it will produce error
print(s)
#s.remove(10)
#print(s)#KeyError: 10

s.discard(4)
print(s)
s.discard(11)
print(s)#there no error produce
s.pop()#remove random element
print(s)
s.clear()#remove all elements mt set is there
print(s)'''
'''s1={1,2,3,4}
s2={1,2,7,8,9}
s3=s1.union(s2)
print(s3)#{1,2,3,4,7,8,9}
s3=s1|s2
print(s3)#{1,2,3,4,7,8,9}
s3=s1.intersection(s2)
print(s3)#{1,2}
s3=s1.difference(s2)
print(s3)#{3,4}
s3=s1-s2
print(s3)#{3,4}
s3=s1.symmetric_difference(s2)
print(s3)#{3,4,7,8,9}'''
'''s1={1,2}
s2={1,2,3,4}
print(s1.issubset(s2))#true'''
'''s1={1,2,3,4}
s2={1,2}
print(s1.issuperset(s2))#true'''
'''s1={1,2,3}
s2={1,2,3}
print(s1.isdisjoint(s2))#False'''
'''s1={1,2,3}
s2={4,5,6}
print(s1.isdisjoint(s2))#True'''

