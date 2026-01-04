#s={1:"sashi",2:"kanth",3:"koppera"}
'''for i in s:
    print(i)#1 2 3''' 
'''for i in s.keys():
    print(i)#1 2 3'''
'''for i in s.values():
    print(i)'''#sashi kanth koppera
'''for i in s.items():
    print(i)'''#(1, 'sashi')
               #(2, 'kanth')
               #(3, 'koppera')
'''print(s.keys())
print(s.values())
print(s.items())'''
#dict_keys([1, 2, 3])
#dict_values(['sashi', 'kanth', 'koppera'])
#dict_items([(1, 'sashi'), (2, 'kanth'), (3, 'koppera')])
d = {"a": 1, "b": 2}
print(d.get("a"))#value access by using key and get method
print(d.get("c"))
d.update({"c":3,"d":4,"e":5})
print(d)#{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
d.pop("a")
print(d)
d.popitem()
print(d)#pop item deletes the last inserted key value pair
#d.clear()
print(d)#remove all items only mt dict is there
d2=d.copy()
print(d2)
print(id(d))
print(id(d2))
d.setdefault("x", 100)
print(d)#add the ithem using setdefault
'''keys=["a","b","c"]
d=dict.fromkeys(keys,0)
print(d)'''#create dict using fromkeys mthod
'''student = {"name": "Ravi", "age": 20}

student["course"] = "Python"
print(student)
print(student.keys())
print(student.values())
print(student.get("age"))
student.update({"age": 21})
student.pop("name")

print(student)'''





