import random
random.seed()

cards = ["ace", "two", "tree", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]
cards_value = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_aces = 0    # Keeps tracks of aces
dealer_aces = 0

# Creating empty lists for the hands to be generated into
dealer_cards = []
dealer_cards_value = []
player_cards = []
player_cards_value = []

player_sum = 0
dealer_sum = 0

while len(dealer_cards) != 2:                                                                   # Generate dealer's cards
    ran = random.uniform(0, 13)
    dealer_cards.append(cards[int(ran)])
    dealer_cards_value.append(cards_value[int(ran)])

while len(player_cards) != 2:                                                                   # Generate player's cards
    ran = random.uniform(0, 13)
    player_cards.append(cards[int(ran)])
    player_cards_value.append(cards_value[int(ran)])

for item in player_cards:  # Keeps tally of player's aces
    if item == "ace":
        player_aces = player_aces + 1
for item in dealer_cards:  # Keeps tally of dealer's aces
    if item == "ace":
        dealer_aces = dealer_aces + 1

if player_aces >= 1:
    player_sum = sum(player_cards_value)-(player_aces-1)*10
else:
    player_sum = sum(player_cards_value)

if dealer_aces >= 1:
    dealer_sum = sum(dealer_cards_value)-(dealer_aces-1)*10
else:
    dealer_sum = sum(dealer_cards_value)



print("player: " + player_cards[0] + " " + player_cards[1], end=" ")
print(player_sum)
print(player_aces)
print("Dealer: " + dealer_cards[0], end=" ")
print(dealer_cards_value[0])

while player_sum <= 20:
    choice = input("stand or hit ")
    if choice == "stand":
        print("Player: ", end="")
        print(player_cards, end="")
        print(player_sum)
        print("Dealer: ", end="")
        print(dealer_cards, end="")
        print(dealer_sum)
        break

    elif choice == "hit":
        ran = random.uniform(0, 13)
        player_cards.append(cards[int(ran)])
        player_cards_value.append(cards_value[int(ran)])
        player_sum = sum(player_cards_value)

        print("Player: ", end="")
        print(player_cards, end=" ")
        print(player_sum)
        print("Dealer: ", end="")
        print(dealer_cards, end=" ")
        print(dealer_sum)

while dealer_sum <= 17:
    ran = random.uniform(0, 13)
    dealer_cards.append(cards[int(ran)])
    dealer_cards_value.append(cards_value[int(ran)])
    if dealer_aces >= 1:
        dealer_sum = sum(dealer_cards_value) - (dealer_aces - 1) * 10
    else:
        dealer_sum = sum(dealer_cards_value) # DU VAR HER: IGANG MED AT FIKSE ACE, SÅ DEN KAN BÅDE VÆRE 1 OG 11, MÅSKE SKAL PLAYER OG FIKSES HELT HVIS MAN MODTAGER ET ACE EFTER ET HIT, ALTSÅ EFTER DE TO FØRSTE, DA DEN NOK KUN HAR TJEKKET EN GANG. :-)
    print("Dealer: ", end="")
    print(dealer_cards, end=" ")
    print(dealer_sum)

if player_sum > 21:
    print("Crash")
elif dealer_sum-player_sum == 0:
    print("tie")
elif dealer_sum-player_sum < 0 or dealer_sum > 21:
    print("win")
elif dealer_sum-player_sum > 0:
    print("lost")
