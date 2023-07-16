'''Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса.'''

'''Доработайте задачу 5.
Вынесите общие свойства и методы классов в класс
Животное.
Остальные классы наследуйте от него.
Убедитесь, что в созданные ранее классы внесены правки.'''


class Animal:
    def __init__(self, name:str=None, breed:str='unknown', age: int = 0):
        self.name = name
        self.breed = breed
        self.age = age

    def print_spec(self):
        return f'специфич_данные'


class Dog(Animal):
    def __init__(self, name:str=None, breed:str='unknown', commands: list[str] = 'unknown'):
        self.name = name
        self.breed = breed
        self.commands = commands

    def print_spec(self):
        return f'{self.commands}'

class Fish(Animal):
    def __init__(self, name: str = None, breed: str = 'unknown', count_fins: list[str] = 'unknown'):
        self.name = name
        self.breed = breed
        self.count_fins = count_fins

    def print_spec(self):
        return f'{self.count_fins}'

class Bird(Animal):
    def __init__(self, name: str = None, breed: str = 'unknown', flights: list[str] = 'unknown'):
        self.name = name
        self.breed = breed
        self.flights = flights

    def print_spec(self):
        return f'{self.flights}'

dog = Dog('Lork', 'Mork', (['Голос', 'Сидеть']))
fish = Fish('Nemo', 'Gold', 3)
bird = Bird('Kedf', 'Попка', 2)

animal = Animal('Леха', 'Cat', 12)

print(animal.print_spec())
print(dog.print_spec())
print(fish.print_spec())
print(bird.print_spec())