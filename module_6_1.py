class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name

class Plant:
    def __init__(self, name):
        self.edible = False
        self.name = name

class Mammal(Animal):
    def eat(self, food):
        if isinstance(food, Plant) and food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Predator(Animal):
    def eat(self, food):
        if isinstance(food, Mammal) and food.alive:
            print(f"{self.name} съел {food.name}")
            self.fed = True
            food.alive = False
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Flower(Plant):
    pass # Flower не является съедобным

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True

# Создаем объекты
lion = Predator("Лев")
zebra = Mammal("Зебра")
apple = Fruit("Яблоко")
rose = Flower("Роза")

# Проверяем взаимодействие
lion.eat(zebra) # Лев съедает зебру
zebra.eat(apple) # Зебра ест яблоко
zebra.eat(rose) # Зебра не ест розу