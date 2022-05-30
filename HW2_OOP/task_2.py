'''
2. Create two classes: Person, Cell Phone, one for composition, another one for aggregation.
  a.
      class Person:
          """
          Make the class with composition.
          """
      class Arm:
          """
          Make the class with composition.
          """
  b.
      class CellPhone:
          """
          Make the class with aggregation
          """
      class Screen:
          """
          Make the class with aggregation
          """
'''


class Person:
    def __init__(self):
        arm_left = Arm('left arm')
        arm_right =Arm('right_arm')
        self.arms = [arm_left.position, arm_right.position]

class Arm:
    def __init__(self, position):
        self.position = position

person = Person()
print(person.arms)


class CellPhone:
    def __init__(self, screen):
        self.screen = screen

class Screen:
    def __init__(self, screen_type='OLED'):
        self.screen_type = screen_type

screen = Screen()
cellphone = CellPhone(screen)
print(cellphone.screen.screen_type)