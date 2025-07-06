import random
from game_data import data
from art import logo, vs

def format_data(account):
    """Takes account data and returns the printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    """Takes user's guess and the follower counts and returns if they got it right"""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

#Generate a random account from the game data
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data) #1

# WHILE LOOP
while game_should_continue:

    # Generate a random account from the game data
    # Make account at position B become the next account at position A
    account_a = account_b #2
    account_b = random.choice(data) #3

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Clear the screen
    print("\n" * 10)
    print(logo)
    # Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score +=1
        print(f"You're right! Current score: {score}")
    if not is_correct:
        print(f"You're wrong. Final score: {score}")
        #game_should_continue = False
        redo = input("Would you like to play again? 'Y' or 'N': \n").lower()
        if redo == 'y':
            game_should_continue = True
            score = 0
        else:
            game_should_continue = False

