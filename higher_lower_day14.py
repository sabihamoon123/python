from art5 import logo
from art5 import vs
from game_data import data
import random


def format_data(account):
    #format the account data into printable frmat 
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"
def check_answer(guess, a_follower, b_follower):
    """Use if statement to check if user is correct"""
    if a_follower > b_follower:
        return guess == "a"
    else:
        return guess == "b"
#display art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)


while game_should_continue:

    #generate random account from the game data
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"compare A: {format_data(account_a)}.")
    print(vs)
    print(f"compare B: {format_data(account_b)}.")

    #sk for user for guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    #check if user is correct
    #get follower count of each account
    a_folloer_count = account_a["follower_count"]
    b_folloer_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_folloer_count, b_folloer_count)

    #give user feedback on their guess
    if is_correct:
        score += 1
        print(f"you're right! Correct score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.")
#use if statement to check if user is correct
