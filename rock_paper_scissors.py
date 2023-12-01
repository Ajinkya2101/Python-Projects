import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images= [rock, paper, scissors]
user= int(input(" 0. Rock\n 1. Paper\n 2. Scissors\n"))
print(game_images[user])

bot_choice= random.randint(0, 2)
if bot_choice == 0:
    print(game_images[bot_choice])
    print("Computer Played: Rock")
if bot_choice == 1:
    print(game_images[bot_choice])
    print("Computer Played: Paper")
if bot_choice == 2:
    print(game_images[bot_choice])
    print("Computer Played: Scissors")

if (user == 0 and bot_choice == 0) or (user == 1 and bot_choice == 1) or (user == 2 and bot_choice == 2):
    print("Draw...")
elif (user == 0 and bot_choice == 2) or (user == 1 and bot_choice == 0) or (user == 2 and bot_choice == 1):
    print("You win :)")
elif (user == 0 and bot_choice == 1) or (user == 1 and bot_choice == 2) or (user == 2 and bot_choice == 0):
    print("You lose:(")
else:
    print("You have entered an invalid number, You lose :(") 