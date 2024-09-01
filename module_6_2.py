class Vehicle:
    __COLOR_VARIANTS = ['red', 'blue', 'green', 'black', 'white']

    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        if new_color.lower() in [color.lower() for color in self.__COLOR_VARIANTS]:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, model, engine_power, color):
        super().__init__(owner, model, engine_power, color)


# Создаем объект класса Sedan
my_sedan = Sedan("Иван Иванов", "Toyota Camry", 200, "black")

# Проверяем работу методов
my_sedan.print_info()
print(my_sedan.get_model())
print(my_sedan.get_horsepower())
print(my_sedan.get_color())

# Попытка сменить цвет (нельзя)
my_sedan.set_color("purple")
my_sedan.set_color("blue")
my_sedan.print_info()