import random
from art import logo
print(logo)
#1 dealing 2 random cards to user and a computer
all_cards = [11,2,3,4,5,6,7,8,9,10,10,10]
# from replit import clear


#main function which runs the program
def deal_cards():
    user_cards = [random.choice(all_cards), random.choice(all_cards)]
    computer_cards = [random.choice(all_cards), random.choice(all_cards)]
    return user_cards, computer_cards


def check_for_blackjack(cards1, cards2):
    if sum(cards1) == 21:
        if sum(cards2) < 21:
            print(f"Your cards: {cards1} your score: {sum(cards1)} – You've got a Blackjack, congratulations!") 
        elif sum(cards2) == 21:
            print(f"Your cards: {cards1} your score: {sum(cards1)} – Both you and a dealer have a Blackjack!")
        print(f"Dealer's cards: {cards2} dealer's score: {sum(cards2)}")
        return True
    else:
        return False


def check_for_bust(cards1, cards2):
    if sum(cards1) > 21:
        if sum(cards2) < 21:
            print(f"Your cards: {cards1} current score: {sum(cards1)} – You're bust, dealer wins") 
        elif sum(cards2) == 21:
            print(f"Your cards: {cards1} current score: {sum(cards1)} – You're bust, dealer has a Blackjack!")
        print(f"Dealer's cards: {cards2} dealer's score: {sum(cards2)}")
        return True
    else:
        return False


def compare_cards(cards1, cards2):
        while sum(cards2) <= 16:
            cards2.append(random.choice(all_cards))
            print(f"Dealer's cards: {cards2} dealer's score: {sum(cards2)}")
            if sum(cards2) >= 21:
                break                
        if sum(cards2) > 21:
            print(f"Your cards: {cards1} current score: {sum(cards1)} – You win, dealer is bust") 
            print(f"Dealer's cards: {cards2} dealer's score: {sum(cards2)}")
        else:
            if sum(cards1) > sum(cards2):
                print(f"Your cards: {cards1} current score: {sum(cards1)} – You win") 
                print(f"Dealer's cards: {cards2} dealer's score: {sum(cards2)}")
            elif sum(cards1) < sum(cards2):
                print(f"Your cards: {cards1} current score: {sum(cards1)} – You lose") 
                print(f"Dealer's cards: {cards2} dealer's score: {sum(cards2)}")
            elif sum(cards1) == sum(cards2):
                print(f"Your cards: {cards1} current score: {sum(cards1)} – It's a push!") 
                print(f"Dealer's cards: {cards2} dealer's score: {sum(cards2)}")

def add_new_card(user_cards, new_card):
    user_cards.append(new_card)
    if (sum(user_cards) >= 21 and 11 in user_cards):
        user_cards.remove(11)
        user_cards.append(1)
    return user_cards
    



def game():
    should_continue = True
    while should_continue:
        if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
            user_cards, computer_cards = deal_cards()
            if check_for_blackjack(cards1=user_cards, cards2=computer_cards) == True:
                should_continue = False
                break
            else:
                print(f"Your cards: {user_cards}, your score: {sum(user_cards)}")
                print(f"Dealer's firsthand : {computer_cards[0]}")
            #giving the user a chance to either hir or stand
                while sum(user_cards) < 21:
                    extra_card = input("Type 'y' to get another card, type 'n' to pass and open up: ").lower()
                    if extra_card == "y":
                        new_card = random.choice(all_cards)
                        user_cards = add_new_card(user_cards, new_card)
                        # user_cards.append(random.choice(all_cards))
                        print(f"Your cards: {user_cards} your score: {sum(user_cards)}")
                        print(f"Dealer's firsthand : {computer_cards[0]}")
                    elif extra_card == "n":
                        print(f"Your cards: {user_cards} your score: {sum(user_cards)}")
                        break
                if check_for_bust(cards1=user_cards, cards2=computer_cards) == True:
                    game()
                    break
                else:
                    should_continue = False
                compare_cards(cards1=user_cards, cards2=computer_cards)
        else:
            print("Bye bye")

game()


