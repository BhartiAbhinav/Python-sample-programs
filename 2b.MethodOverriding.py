#method overriding
class Person:
    def __init__(self):
        self.value=5
    def display(self):
        return self.value
class Student(Person):
    def display(self):
        return self.value+1
s=Student()
print(s.display())
