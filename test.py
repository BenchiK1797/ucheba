class Animal:
    def __init__(self, type, location, age):
        self.type = type
        self.location = location
        self.age = age

    def getInfo(self):
        return {
            "Тип": self.type,
            "Ареал обитания": self.location,
            "Возраст": self.age}

    def setLocation(self):
        location = input("введите среду обитания животного")
        self.location = location
#   _location - меняет тип доступа к атрибуту, предназначен для внутреннего испоьзования,
# пайтон выдаст ошибку. есть риск того что можно изменить атрибут во всем коде
    def run(self):
        return "Бежим вперед"