from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
turns = 0

def check_answers(guess, answer, turns):
    if guess > answer:
        print("Too high:")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"Congtats!!! You got it. The answer was {answer}")

def set_difficulty():
    level = input("Choose a difficulty 'easy' or 'hard' " )
    global turns
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
def game():
    print("Welcome to the guessing game!!!")
    print("I am thinking of a number between 1 to 100...")
    answer = randint(0, 100)

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts left.")
        guess = int(input("Make a guess: "))
        turns = check_answers(guess, answer, turns)
        if turns == 0:
            print("You lose...")
            return


game()
