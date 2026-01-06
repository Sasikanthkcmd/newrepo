'''l=[1,2,3,4,5]
if 2 in l:
    print("yes 2 is present in l")
if 6 not in l:
    print("yes 6 is not present in l")'''
'''output
yes 2 is present in l
yes 6 is not present in l'''
# Membership Operators Demo Program

print("MEMBERSHIP OPERATORS DEMO")
print("-" * 50)

# Using list
nums = [10, 20, 30, 40, 50]
print("List:", nums)

print("10 in nums :", 10 in nums)
print("25 in nums :", 25 in nums)
print("30 not in nums :", 30 not in nums)
print("60 not in nums :", 60 not in nums)
print("-" * 50)

# Using string
text = "Python Programming"
print("String:", text)

print("'P' in text :", 'P' in text)
print("'z' in text :", 'z' in text)
print("'Python' in text :", 'Python' in text)
print("'Java' not in text :", 'Java' not in text)
print("-" * 50)

# Using tuple
data = (1, 2, 3, 4, 5)
print("Tuple:", data)

print("3 in data :", 3 in data)
print("8 in data :", 8 in data)
print("1 not in data :", 1 not in data)
print("-" * 50)

# Using set
s = {100, 200, 300}
print("Set:", s)

print("200 in s :", 200 in s)
print("500 not in s :", 500 not in s)
print("-" * 50)

# Using dictionary (checks keys)
student = {"name": "Vamsi", "roll": 101, "branch": "CSE"}
print("Dictionary:", student)

print("'name' in student :", 'name' in student)
print("'age' in student :", 'age' in student)
print("101 in student :", 101 in student)  # checks keys only
print("-" * 50)

# Membership operator in if condition
print("USING MEMBERSHIP OPERATOR IN IF")

if 20 in nums:
    print("20 found in list")

if 'Python' in text:
    print("Python found in string")

if 'age' not in student:
    print("Age key not present in dictionary")

print("-" * 50)

print("PROGRAM END")
'''output
MEMBERSHIP OPERATORS DEMO
--------------------------------------------------
List: [10, 20, 30, 40, 50]
10 in nums : True
25 in nums : False
30 not in nums : False
60 not in nums : True
--------------------------------------------------
String: Python Programming
'P' in text : True
'z' in text : False
'Python' in text : True
'Java' not in text : True
--------------------------------------------------
Tuple: (1, 2, 3, 4, 5)
3 in data : True
8 in data : False
1 not in data : False
--------------------------------------------------
Set: {200, 100, 300}
200 in s : True
500 not in s : True
--------------------------------------------------
Dictionary: {'name': 'Vamsi', 'roll': 101, 'branch': 'CSE'}
'name' in student : True
'age' in student : False
101 in student : False
--------------------------------------------------
USING MEMBERSHIP OPERATOR IN IF
20 found in list
Python found in string
Age key not present in dictionary
---------------'''

    


