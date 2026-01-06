a=10
b=a
if a is b:
    print("a and b identity is same")
else:
    print("a and b identity is different")
x=5
y=5
if x is not y:
    print("x and y identity is same")
else:
    print("x and y identity is different")
'''out put
a and b identity is same
x and y identity is different'''
if id(a)==id(b):
    print("a and b is same memory location")
else:
    print("a and b is differnet memory location")
if id(x)==id(y):
    print("both points same memory")
else:
    print("different memory")
'''output
a and b is same memory location
both points same memory'''
# Identity Operators Demo Program

print("IDENTITY OPERATORS DEMO")
print("-" * 50)

# Integer identity
a = 10
b = 10
c = 20

print("a =", a, "b =", b, "c =", c)

print("a is b :", a is b)        # Same value, same memory
print("a is c :", a is c)
print("a is not c :", a is not c)
print("-" * 50)

# List identity
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("list1 =", list1)
print("list2 =", list2)
print("list3 =", list3)

print("list1 is list2 :", list1 is list2)      # Different memory
print("list1 == list2 :", list1 == list2)      # Same content
print("list1 is list3 :", list1 is list3)      # Same reference
print("list2 is not list3 :", list2 is not list3)
print("-" * 50)

# Tuple identity
t1 = (10, 20)
t2 = (10, 20)

print("t1 =", t1)
print("t2 =", t2)

print("t1 is t2 :", t1 is t2)
print("t1 == t2 :", t1 == t2)
print("-" * 50)

# String identity
s1 = "Python"
s2 = "Python"

print("s1 =", s1)
print("s2 =", s2)

print("s1 is s2 :", s1 is s2)
print("s1 == s2 :", s1 == s2)
print("-" * 50)

# Identity in if condition
print("USING IDENTITY OPERATOR IN IF")

x = [10, 20]
y = x
z = [10, 20]

if x is y:
    print("x and y refer to the same object")

if x is not z:
    print("x and z refer to different objects")

print("-" * 50)

# Using id() function
print("MEMORY ADDRESSES")
print("id(x) =", id(x))
print("id(y) =", id(y))
print("id(z) =", id(z))

print("-" * 50)
print("PROGRAM END")
'''output
IDENTITY OPERATORS DEMO
--------------------------------------------------
a = 10 b = 10 c = 20
a is b : True
a is c : False
a is not c : True
--------------------------------------------------
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [1, 2, 3]
list1 is list2 : False
list1 == list2 : True
list1 is list3 : True
list2 is not list3 : True
--------------------------------------------------
t1 = (10, 20)
t2 = (10, 20)
t1 is t2 : True
t1 == t2 : True
--------------------------------------------------
s1 = Python
s2 = Python
s1 is s2 : True
s1 == s2 : True
--------------------------------------------------
USING IDENTITY OPERATOR IN IF
x and y refer to the same object
x and z refer to different objects
--------------------------------------------------
MEMORY ADDRESSES
id(x) = 1851091809600
id(y) = 1851091809600
id(z) = 1851091979456
--------------------------------------------------
PROGRAM END
'''
