"""
Допишите код под условия в цикле так, чтобы вывод был корректным
"""


class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        print('?')


class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print('Woof!')


class Cat(Animal):

    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print('Meow!')



animals = [Dog('Dog1'), Dog('Dog2'), Cat('Cat1'), Dog('Dog3')]

for animal in animals:
    animal.speak()
    # Должно выводиться Bark или Meow в зависимости от того какой класс
    pass
