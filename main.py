import random

play_game = 'y'

while (play_game == 'y'):
    answer = random.randint(1, 100)
    try_number = int(input('Guess a number between 1 and 100: '))
    count = 1
    while try_number != answer:
        if try_number > answer:
            print("Your number is too large")
        if try_number < answer:
            print("Your number is too small.")
        try_number = int(input('Guess a number between 1 and 100: '))
        count += 1
    print("You got it! You tried " + str(count) + ' times')
    play_game = input("Continue? (y/n) ").lower()

    if (play_game != "y" or play_game != "n"):
        print("Click y for yes and n for no!")
        play_game = input("Continue? (y/n) ").lower()

    if (play_game == "n"):
        print("See you later...")
