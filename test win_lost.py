import random
random.seed()

cards = ["ace", "two", "tree", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]
cards_value = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

cards_drawn = 0
dealer_aces = 0

for x in range(100):
    dealer_cards = ["four", "jack"]
    dealer_cards_value = [4, 10]
    dealer_sum = sum(dealer_cards_value)

    for item in dealer_cards:               # Count aces in the first hand
        if item == "ace":
            dealer_aces = dealer_aces + 1

    while dealer_sum < 16:
        cards_drawn = cards_drawn + 1

        ran = random.uniform(0, 13)
        dealer_cards.append(cards[int(ran)])
        dealer_cards_value.append(cards_value[int(ran)])

        for item in dealer_cards:
            if dealer_sum + 11 > 21 and item == "ace":
                dealer_sum = sum(dealer_cards_value) - (dealer_aces + 1) * 10
            elif item == "ace" and dealer_aces > 0:
                dealer_sum = sum(dealer_cards_value) - (dealer_aces + 1) * 10
            else:
                dealer_sum = sum(dealer_cards_value)

    print("Dealer: ", end="")
    print(dealer_cards_value, end=" ")
    print(dealer_sum, end=" ")
    print("aces ", end=" ")
    print(dealer_aces)


