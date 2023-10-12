from twoPara import Animal
from  random import randint
animals = []
animalName = ["Заяц","Черепаха","Утка","гусь"."Собаку"]
for name in animalName:
    animals.append(Animal(name,randint(100,200)))

road = int(input("введите длину дороги"))
for animal in animals:
    if animal.getSpeed() >= road:
        print(f"{animal.getType()}пробежал")
    else:
        print(f"{animal.getType()} сошел с дистанции")
