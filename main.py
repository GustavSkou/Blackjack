import random
random.seed()

cards = ["ace", "two", "tree", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]
cards_value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Creating empty lists for the hands to be generated into
dealer_cards = []
dealer_cards_value = []
player_cards = []
player_cards_value = []

x = 2
player_sum = 0

while len(dealer_cards) != 2:                                                                   # Generate dealer's cards
    ran = random.uniform(0, 13)
    dealer_cards.append(cards[int(ran)])
    dealer_cards_value.append(cards_value[int(ran)])

while len(player_cards) != x:                                                                   # Generate player's cards
    ran = random.uniform(0, 13)
    player_cards.append(cards[int(ran)])
    player_cards_value.append(cards_value[int(ran)])

print(dealer_cards[0])
print(player_cards)

while(player_sum <= 20):
    dealer_sum = sum(dealer_cards_value)

    choice = input("stand or hit ")
    if choice == "stand":
        print(dealer_cards[0], end=" ")
        print(dealer_cards[1])
        print(player_cards)
        break

    elif choice == "hit":
        ran = random.uniform(0, 13)
        player_cards.append(cards[int(ran)])
        player_cards_value.append(cards_value[int(ran)])
        player_sum = sum(player_cards_value)

        print(dealer_cards)
        print(player_cards, end=" ")
        print(player_sum)

if player_sum > 21:
    print("Crash")
elif dealer_sum-player_sum == 0:
    print("tie")
elif dealer_sum-player_sum > 0:
    print("win")
elif dealer_sum-player_sum < 0:
    print("lost")
