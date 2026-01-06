'''a=10
b=20
a+=b
print(a)#30
a-=b
print(a)#10
a*=b
print(a)#200
a/=b
print(a)#10.0'''
# Assignment Operators Demo Program

a = 10
b = 5

print("Initial Values")
print("a =", a)
print("b =", b)
print("-" * 40)

# Simple Assignment
a = b
print("After a = b")
print("a =", a)
print("-" * 40)

# Addition Assignment
a += 10      # a = a + 10
print("After a += 10")
print("a =", a)
print("-" * 40)

# Subtraction Assignment
a -= 3       # a = a - 3
print("After a -= 3")
print("a =", a)
print("-" * 40)

# Multiplication Assignment
a *= 2       # a = a * 2
print("After a *= 2")
print("a =", a)
print("-" * 40)

# Division Assignment
a /= 4       # a = a / 4
print("After a /= 4")
print("a =", a)
print("-" * 40)

# Floor Division Assignment
a //= 2      # a = a // 2
print("After a //= 2")
print("a =", a)
print("-" * 40)

# Modulus Assignment
a %= 3       # a = a % 3
print("After a %= 3")
print("a =", a)
print("-" * 40)

# Power Assignment
a **= 3      # a = a ** 3
print("After a **= 3")
print("a =", a)
print("-" * 40)

print("Program End")

