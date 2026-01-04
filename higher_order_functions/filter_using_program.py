#filter() is used to get only required elements from a list based on a condition.
'''n=[1,2,3,4,5,6]
s=list(filter(lambda x:x%2==0,n))
print(s)'''#[2, 4, 6]
'''n=[1,2,3,4,5,6]
s=list(filter(lambda x:x%2!=0,n))
print(s)[1,3,5]'''
'''h=["sashi","rishi","kushi","nani"]
j=list(filter(lambda w:len(w)==5,h))
print(j)['sashi', 'rishi', 'kushi']'''
'''data = ["Python", "", "Java", "", "C"]
result = list(filter(lambda x: x != "", data))
print(result)'''#['Python', 'Java', 'C']




