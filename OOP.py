class Student:
    #properties/attributes
    name ="Eliud"
    gender= "Male"
    age=34

    def study(self):
        print("Student is studying")

    def movement(self):
        print("Student is walking")

student1= Student() #Creating an object
student1.movement()

print(student1.age)


student2= Student()
print(student2.name)


