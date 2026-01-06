'''a=10
print(a>5 and a<15)#True
print(a>5 or a==10)#True
print(not a>15)#True'''
# Logical Operators Demo Program

a = 10
b = 20
c = 5

print("Values:")
print("a =", a)
print("b =", b)
print("c =", c)
print("-" * 40)

# AND operator
print("AND OPERATOR EXAMPLES")
print("a > 5 and b > 15 :", a > 5 and b > 15)#True
print("a > 15 and b > 15:", a > 15 and b > 15)#False
print("a > 5 and b < 10 :", a > 5 and b < 10)#False
print("-" * 40)

# OR operator
print("OR OPERATOR EXAMPLES")
print("a > 5 or b > 25 :", a > 5 or b > 25)#True
print("a > 15 or b > 15:", a > 15 or b > 15)#True
print("a > 15 or b < 10:", a > 15 or b < 10)#False
print("-" * 40)

# NOT operator
print("NOT OPERATOR EXAMPLES")
print("not(a > 5) :", not (a > 5))#False
print("not(a > 15):", not (a > 15))#True
print("-" * 40)

# Logical operators with if condition
print("USING LOGICAL OPERATORS IN IF")

if a > 5 and b > 15:
    print("Both conditions are TRUE")

if a > 15 or b > 15:
    print("At least one condition is TRUE")

if not c > 10:
    print("c is NOT greater than 10")

print("-" * 40)

# Combining multiple logical operators
print("COMBINED LOGICAL CONDITIONS")

if (a > 5 and b > 15) or c == 5:
    print("Combined condition is TRUE")

if not (a < 5 or b < 10):
    print("Inside NOT with OR")

print("-" * 40)

print("PROGRAM END")



