import os
import time
count = 0
def welcome_message():
    print('_________________________Welcome to Silent IPL Auction Program_________________________')
    print("Let's start the auction...")

def display_bidding_status(player, base_price):
    if count == 0:
        print(f"The first bidding is on {player} with a base price of {base_price}.")
    else:
        print(f"The next bidding is on {player} with a base price of {base_price}.")

def get_franchise_name():
    while True:
        franchise = input('Enter the name of your Franchise: ')
        if franchise.strip():
            return franchise
        else:
            print("Franchise name cannot be empty!")

def get_bid_price(base_price):
    while True:
        try:
            price = int(input(f'Enter your bid price (must be greater than {base_price}): '))
            if price > base_price:
                return price
            else:
                print("Price should be greater than the base price.")
        except ValueError:
            print("Please enter a valid number for the bid price.")

def conduct_auction():
    final_bidding_results = {}
    for player, base_price in cricket_players_prices.items():
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console screen
        welcome_message()
        display_bidding_status(player, base_price)
        bidder_data = {}
        bidding_start_time = time.time()
        while True:
            franchise = get_franchise_name()
            price = get_bid_price(base_price)
            bidder_data[franchise] = price
            bidding_end_time = time.time()
            elapsed_time = bidding_end_time - bidding_start_time
            time_remaining = 60 - elapsed_time
            if time_remaining <= 0:
                print("Time's up! Moving to the next player.")
                break
            print(f"Time remaining for {franchise}: {time_remaining:.0f} seconds")
            more = input("Is there anyone else interested? (yes/no): ").lower()
            if more == 'no':
                break
            elif more != 'yes':
                print("Invalid input! Please enter 'yes' or 'no'.")
        highest_bid = max(bidder_data.values(), default=base_price)
        highest_bidder = [franchise for franchise, bid in bidder_data.items() if bid == highest_bid]
        final_bidding_results[player] = {highest_bidder[0]: highest_bid} if highest_bidder else {}
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console screen
    print("Final Bidding Results:")
    for player, bidders in final_bidding_results.items():
        print(f"{player}:")
        for bidder, price in bidders.items():
            print(f"Franchise: {bidder}, Highest Bid: {price}")

# Example cricket players and their base prices
cricket_players_prices = {
    "Virat Kohli": 150000000,
    "Rohit Sharma": 800000,
    "Kane Williamson": 700000,
    "Steve Smith": 900000,
    "Joe Root": 750000,
    "Babar Azam": 2,
    "Ben Stokes": 1200000,
    "Jasprit Bumrah": 1100000,
    "Rashid Khan": 950000,
    "Kagiso Rabada": 1000000,
    "Quinton de Kock": 850000
}

conduct_auction()

