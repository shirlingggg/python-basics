#Encapsulation-bundling of data and methods that operate on the data into a single unit(class).


class Person:
    def __init__(self, name):
        self.name=name

    def getname(self):
        return self.name

    def set_name(self, new_name):
         self.name=new_name

myPerson=Person("Shirleen")
print(myPerson.getname())

myPerson.set_name("Wanjiku")
print(myPerson.getname())

