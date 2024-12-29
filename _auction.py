from art import logo
print(logo)

bidding = True
bid = {}

# def clear_screen():
#     os.system('cls' if os.name == 'nt' else 'clear')


def calculate_highscore(bid):
    high_score = 0
    for key in bid:
        if bid[key] > high_score:
            high_score = bid[key]
    return high_score

user_name = input("What is your name?: ")
user_bid = int(input("What is your bid?: $"))
bid[user_name] = user_bid

while bidding:
    conti = input("Are there any other bidders? Type Y or N: ").lower()
    print("\n"*100)
    if conti == "y":
        user_name = input("What is your name?: ")
        user_bid = int(input("What is your bid?: $"))
        bid[user_name] = user_bid
    elif conti == "n":
        print("Ending the bid")
        bidding = False
    else:
        print("Wrong option. Ending the bid")
        bidding = False


#to get the key and value of the bidder
# print(bid)
highest_bid = calculate_highscore(bid)
highest_bidder = ''
for key, value in bid.items():
    if value == highest_bid:
        highest_bidder = key


print(f"The highest bidding is {highest_bid} \nThe bidding winner is {highest_bidder}  ")

