class Animal:
    """ Родительский класс для классов Мammal и Predator """
    # Живой
    alive = True
    # Накормленный
    fed = False

    def eat(self, food):
        """ Принимает на вход объекты классов растений """
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Mammal(Animal):
    """ Дочерний класс для Animal """
    def __init__(self, name):
        self.name = name


class Predator(Animal):
    """ Дочерний класс для Animal """
    def __init__(self, name):
        self.name = name


class Plant:
    """ Родительский класс для классов Flower и Fruit """
    # Съедобность
    edible = False


class Flower(Plant):
    """ Дочерний класс для Plant """
    def __init__(self, name):
        self.name = name


class Fruit(Plant):
    """ Дочерний класс для Plant """
    edible = True
    def __init__(self, name):
        self.name = name


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)