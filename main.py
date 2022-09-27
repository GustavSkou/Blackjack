import random
random.seed()
import settings

settings.cards
settings.cards_value

money = 100
money_won = 0
money_lost = 0

playing = input("Is it gambling time?(yes/no) ")

while playing == "yes":
    # Creating empty lists for the hands to be generated into
    dealer_cards = []
    dealer_cards_value = []
    player_cards = []
    player_cards_value = []

    player_crash = False
    dealer_crash = False
    player_sum = 0
    dealer_sum = 0
    allow_bet = 0

    print("you have", end=" ")
    print(money)
    bet = input("bet: ")
    Bet = int(bet)
    while allow_bet == 0:
        if Bet <= money:
            money = money - Bet
            allow_bet = 1
        else:
            bet = input("try again. bet: ")
            Bet = int(bet)

    while len(dealer_cards) != 2:                                                       # Generate dealer's first pair of cards and get sum of the cards
        dealer_cards_drawn = len(dealer_cards)                                          # The length of the list is taken before we generate a card, so that it will be -1 the real length. This makes it so we can use it to find the newest card in the hand

        def gen_dealer_card():                                                          # Creating the function to generate a random card
            ran = random.uniform(0, 13)
            dealer_cards.append(settings.cards[int(ran)])
            dealer_cards_value.append(settings.cards_value[int(ran)])
        gen_dealer_card()

        dealer_new_card = dealer_cards_value[dealer_cards_drawn]                        # We use the length of the list from before to find the newest card

        if dealer_cards_value[dealer_cards_drawn] != 11:                                # If the newest card is not an ace we can simply add the cards value to the score
            dealer_sum = dealer_sum + dealer_new_card
        elif dealer_cards_value[dealer_cards_drawn] == 11 and dealer_sum + 11 <= 21:    # If the newest card is an ace and the score plus 11 is 21 or less we can add 11 as the aces value
            dealer_sum = dealer_sum + dealer_new_card
        else:                                                                           # after the 2 statement we know that the card is an ace and the score would exceed 21 so we only add the ace as a 1
            dealer_sum = dealer_sum + 1

    while len(player_cards) != 2:                                                       # Generate player's cards
        player_cards_drawn = len(player_cards)

        def gen_player_card():
            ran = random.uniform(0, 13)
            player_cards.append(settings.cards[int(ran)])
            player_cards_value.append(settings.cards_value[int(ran)])
        gen_player_card()

        player_new_card = player_cards_value[player_cards_drawn]

        if player_cards_value[player_cards_drawn] != 11:
            player_sum = player_sum + player_new_card
        elif player_cards_value[player_cards_drawn] == 11 and player_sum + 11 <= 21:
            player_sum = player_sum + player_new_card
        else:
            player_sum = player_sum + 1

    print("player: " + player_cards[0] + " " + player_cards[1], end=" ")
    print(player_sum)
    print("Dealer: " + dealer_cards[0], end=" ")
    print(dealer_cards_value[0])

    while player_sum < 21:  # Player score is under 21
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
            player_cards_drawn = len(player_cards)
            gen_player_card()
            player_new_card = player_cards_value[player_cards_drawn]

            if player_cards_value[player_cards_drawn] != 11:
                player_sum = player_sum + player_new_card
            elif player_cards_value[player_cards_drawn] == 11 and player_sum + 11 <= 21:
                player_sum = player_sum + player_new_card
            else:
                player_sum = player_sum + 1

            print("Player: ", end="")
            print(player_cards, end=" ")
            print(player_sum)
            print("Dealer: ", end="")
            print(dealer_cards, end=" ")
            print(dealer_sum)

    while dealer_sum < 16:
        dealer_cards_drawn = len(dealer_cards)
        gen_dealer_card()
        dealer_new_card = dealer_cards_value[dealer_cards_drawn]

        if dealer_cards_value[dealer_cards_drawn] != 11:
            dealer_sum = dealer_sum + dealer_new_card
        elif dealer_cards_value[dealer_cards_drawn] == 11 and dealer_sum + 11 <= 21:
            dealer_sum = dealer_sum + dealer_new_card
        else:
            dealer_sum = dealer_sum + 1

        print("Dealer: ", end="")
        print(dealer_cards, end=" ")
        print(dealer_sum)

    if player_sum > 21:
        player_crash = True
    if dealer_sum > 21:
        dealer_crash = True


    if (player_cards_value[0] == 11 and player_cards_value[1] == 10) or (player_cards_value[1] == 11 and player_cards_value[0] == 10):
        money = money + Bet * 3 + Bet
        print("Blackjack +", end="")
        print(Bet*3)
    elif dealer_sum - player_sum == 0 or dealer_crash == True and player_crash == True:
        money = money + Bet
        print("tie")
    elif player_sum > 21:
        print("crash -", end="")
        print(Bet)
    elif dealer_sum - player_sum < 0 or dealer_sum > 21:
        money = money + Bet * 2 + Bet
        print("win +", end="")
        print(Bet*2)
    elif dealer_sum - player_sum > 0:
        print("lost. -", end="")
        print(Bet)

    answer = 0
    while answer == 0:
        playing = input("play again? (yes/no) " )
        if playing == "yes" or "no":
            answer = 1
        else:
            answer = 0
