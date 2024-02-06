import random

score = 0
player_name = input("\nPlease enter your name: ")

while True:
    words = ["python", "computer", "programming",
             "condition", "else", "break", "input",
             "print", "while", "for"]

    pick = random.choice(words)

    random_word = random.sample(pick, len(pick))
    jumbled = "".join(random_word)
    print("\nJumbled word is:", jumbled)

    answer = input("\nWhat's on your mind? ")

    if answer.lower() == pick:
        score += 1
        print("Your score is", score)

        if score == 10:
            print("\nCongratulations", player_name, "you win!")
            print("Your final score is ", score)
            break

    else:
        print("Better luck next time... the correct word is: ", pick)

        cont = input("\npress 'y' to continue and 'n' to quit: ")

        if cont.lower() == "n":
            print("\nAlright", player_name + ", your final score is", score)
            print("Thanks for playing...")
            break
