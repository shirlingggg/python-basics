#Abstraction- hiding complex implementation details while showing only the relevant parts

class Car:
    def start(self):
        print("Car is starting.")
    def stop(self):
        print("Car is stopping.")
myCar=Car()
myCar.start()
myCar.stop()