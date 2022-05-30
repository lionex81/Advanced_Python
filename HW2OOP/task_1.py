"""
1. Create a class hierarchy of animals with at least 5 animals that have additional methods each,
create an instance for each of the animal and call the unique method for it.
Determine if each of the animal is an instance of the Animals class
class Animals:
    Parent class, should have eat, sleep
   class Animal1(Animal):
    Some of the animal with 1-2 extra methods related to this animal
"""


class Animal:
    def eat(self):
        print(f'{self.__class__.__name__} eating')

    def sleep(self):
        print(f'{self.__class__.__name__} sleeping')


class Wolf(Animal):
    def hunt(self):
        print(f'{self.__class__.__name__} hunting')


class Cat(Animal):
    def purr(self):
        print(f'{self.__class__.__name__} purring')


class Kangaroo(Animal):
    def jump(self):
        print(f'{self.__class__.__name__} jumping')


class Otter(Animal):
    def swim(self):
        print(f'{self.__class__.__name__} swimming')


class Snake(Animal):
    def crawl(self):
        print(f'{self.__class__.__name__} crawling')



wolf = Wolf()
cat = Cat()
kangaroo = Kangaroo()
otter = Otter()
snake = Snake()

wolf.hunt()
cat.purr()
kangaroo.jump()
otter.swim()
snake.crawl()

print(f'wolf is an isinstance of the Animal class: {isinstance(wolf, Animal)}')
print(f'cat is an isinstance of the Animal class: {isinstance(cat, Animal)}')
print(f'kangaroo is an isinstance of the Animal class: {isinstance(kangaroo, Animal)}')
print(f'otter is an isinstance of the Animal class: {isinstance(otter, Animal)}')
print(f'snake is an isinstance of the Animal class: {isinstance(snake, Animal)}')


'''
1.a. Create a new class Human and use multiple inheritance to create Centaur class,
 create an instance of Centaur class and call the common method of these classes and unique.

 class Human:
    """
    Human class, should have eat, sleep, study, work
    """

 class Centaur(.. , ..):
    """
    Centaur class should be inherited from Human and Animal and has unique method related to it.
  '''

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name} eating')

    def sleep(self):
        print(f'{self.name} sleeping')

    def study(self):
        print(f'{self.name} studying')

    def work(self):
        print(f'{self.name} working')


class Centaur(Animal, Human):
    def has_six_limbs(self):
        print(f'{self.name} has six limbs')

centaur = Centaur("Hiron", 45)
centaur.eat()
centaur.study()
centaur.has_six_limbs()