'''Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст.'''

class Person:

    def __init__(self, first_name, last_name, phone, age):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self._age = age

    def get_birt(self):
        self._age = self._age + 1

    def get_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_age(self):
        return self._age

human = Person('Илья', 'Захарин', 1234, 50)

print(human.get_age())
print(human.get_birt())
print(human.get_name())