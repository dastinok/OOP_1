'''Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании
экземпляра.
У класса должно быть два метода, возвращающие периметр
и площадь.
Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат.'''


class Square:
    def __init__(self, lenght, width = None):
        self.length = lenght

        if width:
            self.width = width
        else:
            self.width = lenght


    def square(self):
        return self.length * self.width


    def perimiter(self):
        return (self.length + self.width) * 2

square = Square(10)
print(square.square())
print(square.perimiter())