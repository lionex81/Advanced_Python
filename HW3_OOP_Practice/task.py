from abc import ABC, abstractmethod
import random
import time

class Human(ABC):
    @abstractmethod
    def info_about_person(self):
        raise NotImplementedError

    @abstractmethod
    def make_money(self):
        raise NotImplementedError

    @abstractmethod
    def buy_house(self, house):
        raise NotImplementedError



class RealtorMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Person:
    def __init__(self, name, age, money, houses=[]):
        self.name = name
        self.age = age
        self.money = money
        self.houses = houses

    def info(self):
        print(f'My name - {self.name}, I am {self.age} years old. Money on a bank account - {self.money}, houses in property - {len(self.houses)}')

    def make_money(self):
        self.money += 5000
        print(f'Person {self.name} earned money, now {self.name} have {self.money} on a bank account')

    def buy_house(self, house):
        if house.cost <= self.money:
            self.money -= house.cost
            self.houses.append(house)
            print(f'{self.name} buy house: {str(house)}')


class House:
    def __init__(self, cost, area):
        self.area = area
        self.cost = cost

    def apply_discount(self, discount):
        self.cost *= 1 - discount


    def __repr__(self):
        return f'HouseId({id(self)})'


class SmallHouse(House):
    def __init__(self, cost, area=40):
        super().__init__(cost, area)


class Realtor(metaclass=RealtorMeta):
    def __init__(self, name, discount, houses=[]):
        self.name = name
        self.houses = houses
        self.discount = discount

    def info(self):
        print(f'Realtor {self.name} can sold these houses: ' + ', '.join([str(x) for x in self.houses]))

    def give_discount(self):
        return self.discount

    def steal_money(self, person):
        if random.randint(1, 10) == 1:
            person.money = 0
            print(f'Realtor {self.name} steal money. Now {person.name} have {person.money} on a bank account')


if __name__ == '__main__':
    house_0 = House(53000, 75)
    house_1 = House(38000, 55)
    house_2 = SmallHouse(27500)
    house_3 = SmallHouse(26000)

    person_0 = Person('Mike', 30, 20000, [house_2])
    realtor = Realtor('Eric', 0.10, [house_0, house_1, house_3])

    current_count_of_houses = len(person_0.houses)
    while len(person_0.houses) < current_count_of_houses + 1:
        person_0.info()
        realtor.info()
        person_0.make_money()
        realtor.steal_money(person_0)

        discount = 0
        if random.randint(1, 10) == 1:
            discount = realtor.give_discount()
            print(f'Realtor {realtor.name} give discount - {discount}')

        for i in realtor.houses:
            if person_0.money >= i.cost * (1 - discount):
                print(f'Person {person_0.name} can buy {str(i)} for {i.cost * (1 - discount)}')
                i.cost *= (1 - discount)
                person_0.buy_house(i)

        time.sleep(2)