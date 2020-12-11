class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def FunPr(self):
        print("My name is "+self.fname+"  " + self.lname)


class Child(Person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
c = Child("1","2")
c.FunPr()


mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
for x in mystr:
    print(x)








