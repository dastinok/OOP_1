'''Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления
суммы цифр id на семь'''
import random


class Person:

    def __init__(self, first_name, last_name, phone, age):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self._age = age

    def get_birt(self):
        self._age += 1

    def get_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_age(self):
        return self._age



class Stuff(Person):

    def __init__(self, *args, **kwargs):
        self.id = random.randint(100000, 999999)

        super().__init__(*args, **kwargs)
    @property
    def access_lvl(self):
        str_id = str(self.id)
        list_id_num = sum(list(map(int, str_id)))
        return list_id_num % 7

human = Stuff('Илья', 'Захарин', 1234, 50)
print(human.id)
print(human.access_lvl)