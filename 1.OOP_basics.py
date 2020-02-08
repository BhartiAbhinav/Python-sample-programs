class Student:
    Newname='Aayush'
    Newmarks=68
    def __init__(self,a):
        self.a=a

    def add(self):
        n = int(input())
        for i in range (n):
            name=input()
            marks=int(input())
            self.a=a.append(name)
            self.a=a.append(marks)
        print(a)
a=list()
s=Student(a)
s.add()
print(getattr(s,'Newname',67))
setattr(s,'Newname','Satyam')
print(getattr(s,'Newname',56))
print(hasattr(s,'Oldname'))
delattr(Student,'Newmarks')
print(hasattr(s,'Newmarks'))