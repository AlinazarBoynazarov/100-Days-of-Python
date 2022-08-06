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

#Write your code below this line 👇

import random

game_images = [rock, paper, scissors]

choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n'))
if choice >= 3 or choice < 0:
    print('You\'ve entered an invalid number, please restart and try again')

else:
    print(game_images[choice])


    comp_choice = random.randint(0, 2)
    print(f"Computer chose: {game_images[comp_choice]} ")


    if choice == 0 and comp_choice == 2:
        print('You win!')
    elif choice == 2 and comp_choice == 0:
        print('You lose')
    elif choice > comp_choice:
        print('You win')
    elif choice < comp_choice:
        print('You lose')
    elif comp_choice == choice:
        print('It\'s a draw, please run it again')















