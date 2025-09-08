class Animal():
    """Создаем животное"""
    def __init__(self, name:str, age:int, height:int):
        """Инициализируем атрибуты животного"""
        self.name = name
        self.age = age
        self.height = height
        self.weight = 10

    def description_puppy(self):
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

