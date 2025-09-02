class Person():
    """Модель человека""" # описание класса

    def __init__(self, name:str, age:int): # __init__ инициализация класса в конструкторе указываем параметры класса
        """Инициализация атрибутов человека - имя, возраст"""
        self.name = name # self - это ссылка на экземпляр класса (обязательно в начале добавляем self)
        self.age = age
        print("Человек создан")

    def sing(self): # методы класса, то что способен делать экземпляр класса
        """Просим человека спеть"""
        print(self.name + " поет")

    def dance(self):
        """Просим человека станцевать"""
        print(self.name + " танцует")

    def walk(self):
        """Просим человека погулять"""
        print(self.name + " гуляет")

man = Person("Max", 33)
woman = Person("Nasty", 28)


man.dance()
woman.dance()
man.walk()
