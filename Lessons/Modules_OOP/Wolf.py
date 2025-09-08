from Lessons.Modules_OOP.Base_animal import Animal

class Wolf(Animal):
    """Создаем класс волка"""

    def __init__(self, name: str, age: int, height: int):
        """Инициализируем атрибуты класса родителя"""
        super().__init__(name, age, height)
        self.rage = 100

    def get_rage(self):
        """Получение заряда ярости"""
        print("Заряд ярости волка равен: " + str(self.rage))

    def description_puppy(self):
        """Получение описания волка"""
        description = (self.name
                       + ", ему: " + str(self.age)
                       + " лет, " + "заряд ярости: " + str(self.rage))
        print("Нового волка зовут: " + description)
        return description


dog = Animal("Max", 10, 52)  # экземпляр класса предка
dog.description_puppy()  # описание экземпляра класса предка
dog.get_weight()
# dog.update_weight(10)   # поправился на 10 кг
# dog.update_weight(-5)   # похудел на 5 кг
# dog.get_weight()

wild_wolf = Wolf("Дымок", 2, 45)  # экземпляр класса потомка
wild_wolf.description_puppy()
