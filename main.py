# from test import Animal
# from test1 import Car
#
# wolf = Animal("волк","лес",12)
# pig = Animal("свинья","город",4)
# animals = [wolf,pig]
# for animal in animals:
#     print(animal.getInfo())
#     # animal.setLocation()
#
# car = Car()
# car.setMotor(wolf)
# print(car.forward())



# from twoPara import Animal
# from random import  randint
# animal1 = Animal("Заяц",randint(100,200))
# animal2 = Animal("Волк",randint(100,200))
# animal3 = Animal("Утка",randint(100,200))
# animals = [animal1,animal2,animal3]
# road = int(input("введите длину дороги"))
# for animal in animals:
#     if animal.getSpeed() >= road:
#         print(f"{animal.getType()} пробежал")
#     else:
#         print(f"{animal.getType()} сошел с дистанции")


from adacha import Cars
car1 = Cars("универсал","дизельный","черный")
car2 = Cars("седан","бензиновый","красный")
car3 = Cars("хетчбэк","на газу","синий")
cars = [car1,car2,car3]
zapros = int(input("ведите номер комплектации"))-1
print(cars[zapros].getInfo())
# carBody= []
# carMotor=[]
# carColor=[]
# for body in carBody:
#     print(body)
# body = carBody[int(input())]
# ...
# car = Cars(body,motor,color)
#

