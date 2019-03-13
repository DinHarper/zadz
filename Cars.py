class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print("Машина {} поехала".format(self.name))

    def stop(self):
        print("Машина {} остановилась".format(self.name))

    def turn(self, dirt):
        print("Машина {} повернула" .format(self.name))


class TownCar(Car):
    def __init__ (self, speed, color, name):
        Car.__init__(self,speed,color,name)


class SportCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name)


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name)
        self.is_police = True


my_car = Car(60, 'Black', 'Volga')

my_car.go()
my_car.turn('Направо')
my_car.stop()
input()
