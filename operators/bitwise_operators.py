'''a=10
b=20
print(a&b)#0
print(a|b)#30
print(a^b)#30
print(~b)#21
print(a<<1)#20
print(b>>2)#5'''
# Bitwise Operators Demo Program

a = 10   # Binary: 1010
b = 6    # Binary: 0110

print("Initial Values")
print("a =", a, "->", bin(a))
print("b =", b, "->", bin(b))
print("-" * 50)

# Bitwise AND
print("BITWISE AND (&)")
print("a & b =", a & b)
print("Binary :", bin(a & b))
print("-" * 50)

# Bitwise OR
print("BITWISE OR (|)")
print("a | b =", a | b)
print("Binary :", bin(a | b))
print("-" * 50)

# Bitwise XOR
print("BITWISE XOR (^)")
print("a ^ b =", a ^ b)
print("Binary :", bin(a ^ b))
print("-" * 50)

# Bitwise NOT
print("BITWISE NOT (~)")
print("~a =", ~a)
print("~b =", ~b)
print("-" * 50)

# Left Shift
print("LEFT SHIFT (<<)")
print("a << 1 =", a << 1)
print("Binary :", bin(a << 1))
print("a << 2 =", a << 2)
print("Binary :", bin(a << 2))
print("-" * 50)

# Right Shift
print("RIGHT SHIFT (>>)")
print("a >> 1 =", a >> 1)
print("Binary :", bin(a >> 1))
print("a >> 2 =", a >> 2)
print("Binary :", bin(a >> 2))
print("-" * 50)

print("Program End")

'''output
Initial Values
a = 10 -> 0b1010
b = 6 -> 0b110
--------------------------------------------------
BITWISE AND (&)
a & b = 2
Binary : 0b10
--------------------------------------------------
BITWISE OR (|)
a | b = 14
Binary : 0b1110
--------------------------------------------------
BITWISE XOR (^)
a ^ b = 12
Binary : 0b1100
--------------------------------------------------
BITWISE NOT (~)
~a = -11
~b = -7
--------------------------------------------------
LEFT SHIFT (<<)
a << 1 = 20
Binary : 0b10100
a << 2 = 40
Binary : 0b101000
--------------------------------------------------
RIGHT SHIFT (>>)
a >> 1 = 5
Binary : 0b101
a >> 2 = 2
Binary : 0b10
--------------------------------------------------
Program End
'''
