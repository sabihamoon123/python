from art1 import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder (bidding_record):
    highest_bid = 0
    winner =""
    # bidding_record = {"Moon" : 123, "Asif" : 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with bid of ${highest_bid}") 



while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there were any other bidders? 'Yes' or 'No'? ")
    if should_continue == "No":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "Yes":
        print("Clear")