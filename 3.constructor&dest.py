class Students:

    def __init__(self,counter,name,age):
        self.counter=counter+1
        self.name=name
        self.age=age

    def func(self):
        return self.counter
    def __del__(self):
        print("class is destroyed")
s=Students(0,"name",22)
print(s.func())