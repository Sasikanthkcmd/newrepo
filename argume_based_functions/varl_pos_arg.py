'''def fun_c(*arg):
    for i in arg:
        print(i,end=" ")
fun_c(5,8,"a",8)#5 8 a 8'''
'''def show(*nums):
    print(nums)
show(10, 20, 30, 40)'''#(10, 20, 30, 40)
'''def sum_of_nums(*n):
    s=0
    for i in n:
        s=s+i
    return s
h=sum_of_nums(10,20,30,40)
print(h)#100'''
def student(name, *marks):
    print("Name:", name)
    print("Marks:", marks)

student("Sashi", 80, 85, 90)


       
