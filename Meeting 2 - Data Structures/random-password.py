import random
import string

print("\nWelcome to Password Maker!\n")

adjectives_list = ["sleepy", "slow", "fluffy", "red", "yellow", "green", "blue"]
nouns_list = ["Dinosaur", "Ball", "Dragon", "Hammer", "Apple", "Duck", "Panda"]

adjective = random.choice(adjectives_list)
noun = random.choice(nouns_list)
number = random.randrange(0, 100)
char = random.choice(string.punctuation)

password = adjective + noun + str(number) + char
print("Recommended Password : " + password)

usernames_list = ["harry", "arsham", "ali"]
username = random.choice(usernames_list)

email = username + adjective + str(number)
print("Recommended Email    : " + email + "@mail.com")
