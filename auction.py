
bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
            print(f"The winner is {winner} and the highest bid is {highest_bid}")

while not bidding_finished:
    name = input("Name of the current bidedr: ")
    price = input("Enter your bid: ")
    price = int(price)
    bids[name] = price
    should_continue = input("Any further bidders? Type 'yes' or 'no'. ")
    if should_continue == "no":
        bidding_finished = True
