class Person:

    # constructor
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def say_hello(self):
        print(f'\nHello {self.name}, nice to meet you!')

    def ride(self):
        self.say_hello()
        if self.age > 10 and self.height >= 100:
            print(f'Congratulations {self.name}! You may ride the roller coaster.')
        else:
            print(f'Sorry {self.name}, you may not ride the roller coaster.')


# objects
james = Person("James", 10, 140)
rose = Person("Rose", 12, 150)
dove = Person("Dove", 12, 150)
diva = Person("Diva", 8, 130)

while True:

    person_name = input("\nEnter name: ")

    if person_name == 'James':
        james.ride()
    elif person_name == 'Rose':
        rose.ride()
    elif person_name == 'Dove':
        dove.ride()
    elif person_name == 'Diva':
        diva.ride()
    else:
        print("Sorry, you haven't registered yet!")

    answer = input("\nPress 'y' to continue / 'n' to quit: ")

    if answer.lower() == 'n':
        break
