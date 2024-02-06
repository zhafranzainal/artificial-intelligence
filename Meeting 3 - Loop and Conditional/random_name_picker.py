import random

names = []

print("\nAdd names to shuffle! \nPress 'S' to stop\n")

while True:
    add_name = input('Add name: ')

    if add_name.lower() != 's':
        names.append(add_name)
    else:
        if not names:
            print("\nError! No names added, please add names before stopping.\n")
        else:
            random_name = random.choice(names)
            print("\nChosen person: " + random_name)
        break
