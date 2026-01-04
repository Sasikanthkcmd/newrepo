#s=[1,2,4,3,6,5]
'''s.append(7)#add element last
print(s)'''
'''s.insert(3,8)#add element at specific position
print(s)'''
'''s.insert(4)
print(s)#TypeError: insert expected 2 arguments, got 1'''
'''s.remove(4)
print(s)'''#just remove the elemnet
'''s.pop(3)
print(s)'''#remove the element base on the index
'''s.sort
   print(s)'''#sort the list elements
'''print(sorted(s))#print and sort the list'''
'''sorted(s)
print(s)'''#print the original list dont print the sorted listi
'''s.reverse()
print(s)'''#reverse the list
'''s.clear()
print(s)'''#clear all list elements mt list is there
#NESTED LIST
#t=[[1,2,3],[4,5,6,7],[8,9]]
'''print(t[0])#[1, 2, 3]
print(t[1][2])#6
print(t[0][1])#2
print(t[2][0])#8
print(t)#[[1, 2, 3], [4, 5, 6, 7], [8, 9]]'''
'''data = [["Sasi", 22], ["Ravi", 21], ["Anu", 23]]
print(data)#[['Sasi', 22], ['Ravi', 21], ['Anu', 23]]
print(data[0][0])#sasi
print(data[1][1])#21'''
#print nexted list elements using for loop
s=[[1,2,3,4],[5,6,7,8],[9,0]]
'''for i in s:
    for j in i:
        print(j,end=" ")'''#1 2 3 4 5 6 7 8 9 0

'''i=0
while i<len(s):
    j=0
    while j<len(s[i]):
        print(s[i][j],end=" ")#1 2 3 4 5 6 7 8 9 0
        j=j+1
    i=i+1'''#while loop used to print the nexted list elements
l=[]
for i in range(5):
    if len(l)<5:
        n=int(input("enter the num"))
        l.append(n)
print(l)          


    
    


        










