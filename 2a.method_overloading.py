#method overloading
class Person:
    def area(self,l=None,b=None):
        self.l=l
        self.b = b
        if l!=None and b!=None:
            ar=l*b
        else:
            ar=l*l*3.14
        print(ar)
s=Person()
s.area(2)