s = "  Python Programming 123  "
# Case conversion
print("original string:",s)
print("upper():",s.upper())
print("lower():",s.lower())
print("capitalize():",s.capitalize())
print("title():",s.title())
print("swapcase():",s.swapcase())
print("-" *40)
# Checking methods
print("isupper()",s.isupper())#False
print("islower()",s.islower())#False
print("isalpha()","python".isalpha())#True
print("isalpnum()","python123".isalnum())#True
print("isspace():","  ".isspace())#True
print("isdigit():","123".isdigit())#True
print("-"*40)
# Strip methods
print("isstrip():",s.strip())#removethe spaces  left hand side and right hand side
print("lstrip():",s.lstrip())#remove the spaces only in left side
print("rstrip():",s.rstrip())#remove spaces only in right side
print("-"*40)
## Searching methods
print("find('Python'):", s.find("Python"))#it returns starting index of substrin incase if not found return -1
print("index('Programming'):", s.index("Programming"))#it retuirns the starting index of substring it not found it will produce the error
print("count('o'):", s.count("o"))#count how many times a character appears and return the value
print("-"*40)
#replace
print(s.replace("Python","c"))
print("-"*40)      
words=s.split()
print("split():",words)
joined = "-".join(words)
print("join():", joined)#join(): Python-Programming-123
some="*".join(s)
print(some)# * *P*y*t*h*o*n* *P*r*o*g*r*a*m*m*i*n*g* *1*2*3* *
#join used in any iterable syntax is like this
#saparator.join(iterable")
## Start & End checks
print("startswith('  Python'):", s.startswith("  Python"))
print("endswith('123  '):", s.endswith("123  "))
'''Important Rule
startswith() and endswith() are checking methods
They never raise errors
They return only True or False'''
print("-" * 40)
'''text = "Hi"

print("center():", text.center(10, "*"))
print("ljust():", text.ljust(10, "*"))
print("rjust():", text.rjust(10, "*"))

center(): ****Hi****
ljust(): Hi********
rjust(): ********Hi'''
