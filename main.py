from replit import clear
from art import logo
print(logo)

print("Welcome to the secret auction program.")
list_of_input = {}

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")


should_continue = True
while should_continue:
    name = input("What is your name? ")
    bid = int(input("What is your bid?$ "))
    list_of_input[name] = bid
    restart = input("Are there any other bidders? Type 'yes' or 'no'.  ")
    clear()

    if restart=="no":
        should_continue = False
        find_highest_bidder(list_of_input)


