from art import logo
from art import vs
from game_data import data
from replit import clear
import random
from replit import clear


#comparing values A, B against the user guess
def compare(value_A, value_B, ans):
    """comparing values A, B against the user guess"""
    if ans == 'A':
        if value_A['follower_count'] > value_B['follower_count']:
            return True
        else:
            return False
    elif ans == 'B':
        if value_A['follower_count'] < value_B['follower_count']:
            return True
        else:
            return False


#main function
def game():
    # should_continue = True
    should_continue = True
    playing = True

    score = 0
    print(logo)

    while should_continue:  

        A = random.choice(data)
        B = random.choice(data)
        if A == B:
            B = random.choice(data)

        while playing:

            print(f"Compare A: {A['name']}, {A['description']}, from {A['country']}")
            print(vs)
            print(f"Against B: {B['name']}, {B['description']}, from {B['country']}")

            answer = input("Who has more followers? ")

            clear()

            if compare(A, B, answer) == True:
                score += 1
                print(f"You're right! Current score: {score}")
                A = B
                B = random.choice(data)
                
            elif compare(A, B, answer) == False:
                break
        break
        
    print(f"Sorry, that's wrong. Final score: {score}")

game()

 


