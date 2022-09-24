import random
random.seed()

cards = ["ace", "two", "tree", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]
cards_value = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

for x in range(1000):
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

    for item in player_cards:                                                                       # Keeps tally of player's aces
        if item == "ace":
            player_aces = player_aces + 1
    if player_aces >= 1:
        player_sum = sum(player_cards_value)-(player_aces-1)*10
    else:
        player_sum = sum(player_cards_value)

    for item in dealer_cards:                                                                       # Keeps tally of dealer's aces
        if item == "ace":
            dealer_aces = dealer_aces + 1
    if dealer_aces >= 1:
        dealer_sum = sum(dealer_cards_value)-(dealer_aces-1)*10
    else:
        dealer_sum = sum(dealer_cards_value)

    print("player: " + player_cards[0] + " " + player_cards[1], end=" ")
    print(player_sum)
    print("Dealer: " + dealer_cards[0], end=" ")
    print(dealer_cards_value[0])

    while player_sum <= 20:
        choice = "stand"
        #input("stand or hit ")
        if choice == "stand":
            print("Player: ", end="")
            print(player_cards, end="")
            print(player_sum)
            print("Dealer: ", end="")
            print(dealer_cards, end="")
            print(dealer_sum)
            break

        elif choice == "hit":
            player_aces = 0
            ran = random.uniform(0, 13)
            player_cards.append(cards[int(ran)])
            player_cards_value.append(cards_value[int(ran)])

            for item in player_cards:                                                               # Keeps tally of player's aces
                if item == "ace":
                    player_aces = player_aces + 1
            if player_aces >= 1:
                player_sum = sum(player_cards_value) - (player_aces - 1) * 10
            else:
                player_sum = sum(player_cards_value)

            print("Player: ", end="")
            print(player_cards, end=" ")
            print(player_sum)
            print("Dealer: ", end="")
            print(dealer_cards, end=" ")
            print(dealer_sum)

    while dealer_sum < 16:
        ran = random.uniform(0, 13)
        dealer_cards.append(cards[int(ran)])
        dealer_cards_value.append(cards_value[int(ran)])

        dealer_aces = 0  # Sets dealer_aces to 0 again, so we can use the fuction from before again
        for item in dealer_cards:  # Keeps tally of dealer's aces
            if item == "ace":
                dealer_aces = dealer_aces + 1  # 1'

        if dealer_aces > 1:
            dealer_sum = sum(dealer_cards_value) - (dealer_aces - 1) * 10
        else:
            dealer_sum = sum(dealer_cards_value)

        print("Dealer: ", end="")
        print(dealer_cards, end=" ")
        print(dealer_sum, end=" ")
        print("aces ", end=" ")
        print(dealer_aces)

    if player_sum > 21:
        print("Crash")
    elif dealer_sum-player_sum == 0:
        print("tie")
    elif dealer_sum-player_sum < 0 or dealer_sum > 21:
        print("win")
    elif dealer_sum-player_sum > 0:
        print("lost")

