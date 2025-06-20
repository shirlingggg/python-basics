#Built-in functions/Standard library functions

x = max(67, 89, 90, 23, 45, 55)
print("The maximum number is", x)

y= min(67, 89, 90, 23, 45, 55)
print("The minimum number is", x)

z=pow(2, 3)
print("The power of 2 is", z)
print()



#User-defined functions
def greeting():
    print("Hello world!")

greeting() #Calling a function
print()


def school():
    print("My coding school is eMobilis.")
school()
print()



#Parameters and arguments
def add(num1, num2):
    print(num1+num2)

add(5, 10)
add(20, 10)
add(4, 8)

print()

def student(fullname, course, gender):
    print(fullname, course, gender)

student("Mary Mbotela", "MIT", "Female")
student("James Kamau", "MIT", "Male")
student("Mary Mbotela", "MIT", "Female")
student("Mary Mbotela", "MIT", "Female")
student("Mary Mbotela", "MIT", "Female")
print()

#A Python program that displays details of 5 employees at FinTech using parameters and arguments(Fullname, email, age, position, salary, marital status)

def employees(fullname, email, age, position, salary, marital_status):
    age=int(age)
    salary=float(salary)
    print(fullname, email, age, position, salary, marital_status)

employees("Kamau Njoroge", "kamau@gmail.com", 30, "Receptionist", 30000, "single")
employees("Amina Yusuf", "amina@gmail.com", 27, "Graphic designer", 54000.67, "single")
employees("Brian Otieno", "brian@gmail.com", 33, "Project Manager", 50000, "married")
employees("Kamau Njoroge", "kamau@gmail.com", 30, "Receptionist", 43000, "single")
employees("Kamau Njoroge", "kamau@gmail.com", 30, "Receptionist", 43000, "single")
