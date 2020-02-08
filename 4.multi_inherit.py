class Person:
    def define(self,name,age):
        self.name=name
        self.age=age
        print(name)
        print(age)
class Student(Person):
    def mark(self,marks):
        self.marks=marks
        print(marks)
        s.define("AAyush",22)
class Locality(Student):
    def add(self,address):
        self.address=address
        print(address)
        s.mark(69)
s=Locality()
s.add("Tower 15. 704")