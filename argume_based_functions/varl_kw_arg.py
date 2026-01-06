def some_c(**kw):
    print(type(kw))
    for i,j in kw.items():
        print(i,":",j)
some_c(name="sashi",office="thundersoft",role="intern")
#<class 'dict'>
#name : sashi
#office : thundersoft
#role : intern
def student(id, **details):
    print("ID:", id)
    for k, v in details.items():
        print(k, "=", v)

student(101, name="Ravi", marks=85)
#ID: 101
#name = Ravi
#marks = 85



