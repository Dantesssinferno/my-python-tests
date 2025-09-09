class Car:
    """Класс по созданию и работе с машиной"""
    def __init__(self, model:str, year:int, engine:float, price:float, mileage:float):
        """Атрибуты класса"""
        self.model = model
        self.year = year
        self.engine = engine
        self.price = price
        self.mileage = mileage
        self.wheels = 4
        print("Новая машина создана")

    def description(self):
        """Получение описания машины"""
        description = (f'Модель машины : {self.model}, '
                       f'год выпуска : {self.year}, '
                       f'объем двигателя : {self.engine}, '
                       f'цена : {self.price}, '
                       f'пробег : {self.mileage} миль',
                       f'колес : {self.wheels}'
                       )
        print(description)

class Truck(Car):
    """Класс по созданию и работе с грузовиком"""
    def __init__(self, model:str, year:int, engine:float, price:float, mileage:float):
        super().__init__(model, year, engine, price, mileage)
        """Инициализируем атрибуты класса родителя"""
        self.wheels = self.wheels + 4
        print(f'Новый Грузовик создан : {model}')

Toyota = Car("Supra", 2025, 3, 45000, 1000)
Toyota.description()

Mersedes = Truck("MLL-980", 2025, 5.6, 1500, 1500)
Mersedes.description()

