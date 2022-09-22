import random
random.seed()

cards = ["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"]
cards_value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Creating empty lists for the hands to be generated into
dealer_cards = []
dealer_cards_value = []
player_cards = []
player_cards_value = []

while len(dealer_cards) != 2:                                                                   # Generate dealer's cards
    ran = random.uniform(0, 13)
    dealer_cards.append(cards[int(ran)])
    dealer_cards_value.append(cards_value[int(ran)])

while len(player_cards) != 2:                                                                   # Generate player's cards
    ran = random.uniform(0, 13)
    player_cards.append(cards[int(ran)])
    player_cards_value.append(cards_value[int(ran)])

dealer_sum = sum(dealer_cards_value)
player_sum = sum(player_cards_value)
print(dealer_cards, end=" ")
print(dealer_sum)
print(player_cards, end=" ")
print(player_sum)
