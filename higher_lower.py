logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

import random
from higher_lower_game_data import data

def get_random_acc():
    return random.choice(data)

def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_answers(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
    
def game():
    print(logo)
    score = 0
    game_should_continue = True
    account_a = get_random_acc()
    account_b = get_random_acc()

    while game_should_continue:
        account_a = account_b
        account_b = get_random_acc()

        while account_a == account_b:
            account_b = get_random_acc()
            
            print(f"Compare A: {format_data(account_a)}.")
            print(vs)
            print(f"Compare B: {format_data(account_b)}.")

            guess = input("Who has more followers 'A' or 'B'? \n").lower()
            a_follower_count = account_a["follower_count"]
            b_follower_count = account_b["follower_count"]
            is_correct = check_answers(guess, a_follower_count, b_follower_count)

            print(logo)
            if is_correct:
                score += 1
                print(f"You're right! Current score: {score}.")
            else:
                game_should_continue = False
                print(f"Sorry, that's wrong. Final score: {score}")

game()

