class Dog:
    def __init__(self, name, breed, age, color):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color


    def sound(self):
        print(self.name, "is barking.")

dog1 = Dog("Victory", "German Shepherd", 5, "White")
print(dog1.name)
dog1.sound()


dog2 = Dog("Braxton", "Siberian Husky", 2, "Brown")
print(dog2.breed, dog2.age, dog2.color)
dog2.sound()

dog3 = Dog("Abigail", "Chihuahua", 5, "White")
print(dog3.color)


