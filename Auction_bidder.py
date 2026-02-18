""" Finding highest bidder
You are going to write a program for a bidding auction. The program will
ask for the names of the bidders and the amount they are bidding. Then it should find the highest bidder 
and how much they bid."""



bids ={}



def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")



continue_bidding = True
while continue_bidding:
    name = input("What is your name? ")
    price =int(input("What is the price of the bid? $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    else:
        print("*" * 20)