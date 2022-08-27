from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
print("Welcome to the secret auction program.")

bidding_continues = True
bids = {}
    

def highest_bidder(dictionary):
    highest_bid = 0
    winner_name = ""
    for bidder in dictionary:
        bid_amount = dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner_name = bidder
    print(f"The winner is {bidder} with a bid of ${highest_bid}")

    

while bidding_continues:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  question = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if question == "no":
    bidding_continues = False
    highest_bidder(bids)
  elif question == "yes":
    clear()



  
  













