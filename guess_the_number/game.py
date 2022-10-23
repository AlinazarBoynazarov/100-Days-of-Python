import random
from art import logo
from replit import clear
# should_continue = True
difficulty = {"easy": 10, "hard": 5}
should_continue = True


#setting the difficulty
def set_difficulty():
    dif = input("Choose a diffuculty level. Type 'easy' or 'hard': ")
    return difficulty[dif]
    
def check(num_guess, ran_num):
        #checking
    if num_guess == ran_num:
        print("You guessed it right!")
        return True
    else:
        if num_guess < ran_num:
            print("Too Low")
        if num_guess > ran_num:
            print("Too High")

def game():
    print(logo)
    global should_continue
    while should_continue:
        numb = random.randrange(1, 100)
        print("Welcome to the Number Guessing Game!")
        print("I am thinking of a number between 1 and 100.")
        level = set_difficulty()
        
        print(f"You have {level} attempts remaining to guess the number. ")

        for i in range(level):
            guess = int(input('Make a guess: '))
            if check(num_guess=guess, ran_num=numb) == True:
                quit()
        play = input(f"You ran out of trials. Would you like to play more? Type 'yes' or 'no': ").lower()
        if play == "yes":
            break
        elif play == "no":
            print("Thank you, hope you enjoyed it!")
            quit()
    clear()     
    game()

game()









                    


        














