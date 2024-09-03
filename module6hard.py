import math

class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = color
        self.filled = False
        if len(sides) == self.sides_count:
            self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count

    def get_color(self):
        return list (self.__color)

    def __is_valid_color(self, r, g, b):
        return all(0 <= value <= 255 for value in (r, g, b)) and all(isinstance(value, int) for value in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, side):
        super().__init__(color, side)
        self.__radius = side / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius*2

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        s = sum(self.__sides) / 2
        return math.sqrt(s * (s - self.__sides[0]) * (s - self.__sides[1]) * (s - self.__sides[2]))

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side):
        cube_sides = [side] * self.sides_count
        super().__init__(color, *cube_sides)


    def get_volume(self):
        return self.get_sides()[0]**3


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)



print(f"Цвет круга: {circle1.get_color()}")
print(f"Площадь круга: {circle1.get_square()}")
print(f"Цвет куба: {cube1.get_color()}")
print(f"Объем куба: {cube1.get_volume()}")

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())