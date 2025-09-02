class Animal():
    """Создаем животное"""

    def __init__(self, name, age, height):
        """Инициализируем атрибуты животного"""
        self.name = name
        self.age = age
        self.height = height
        self.weight = 100

    def description_person(self):
        """Получение описания животного"""
        description = (self.name
                       + ", ему: " + str(self.age)
                       + " лет, " + "рост: " + str(self.height)
                       + " см" + ", вес: " + str(self.weight) + " кг")
        print("Нового питомца зовут: " + description)

    def get_weight(self):
        """Получение веса питомца"""
        print("Вес питомца: " + str(self.weight) + " кг")

    def update_weight(self, kg):
        """Изменение веса человека"""
        self.weight = self.weight + kg
        print("Вес изменился на: " + str(kg) + " кг")
        print("Текущий вес: " + str(self.weight) + " кг")



dog = Animal("Max", 10, 52)

dog.get_weight()
dog.update_weight(10)   # поправился на 10 кг
dog.update_weight(-5)   # похудел на 5 кг
dog.get_weight()


