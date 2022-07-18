import random
from art import logo
cards= ['ACE', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Q' , 'J','K']

def card_score(cards):
    ace=False
    sum=0
    for i in cards:
        if i =='ACE':
            sum+=11
            ace=True
        elif i=='Q' or i =='K' or i=='J':
            sum+=10
        else:
            sum+=i
        if sum>21 and ace:
            sum-=10
    return sum

def take_card(hand):
    new_card=random.choice(cards)
    hand.append(new_card)

def print_player_cards(hand):
    print(f"Your cards : {hand}       current score: {card_score(hand)}")

def print_dealer_cards(hand,final):
    if final:
        print(f"Dealer's Final cards : {hand}  final Score: {card_score(hand)}")
    else:
        print(f"Dealer's cards : {hand[0]}")





print(logo)
start_game=input("Want to start playing BlackJack? Type 'y' to start : ")
while start_game=='y':
    Player_hand = []
    Dealer_hand = []
    for i in range(2):
        take_card(Player_hand)
        take_card(Dealer_hand)
    print_player_cards(Player_hand)
    print_dealer_cards(Dealer_hand,False)
    taking_card=True
    while card_score(Player_hand) <=21 and taking_card:
        take=str(input("Type 'y' to get another card, type 'n' to pass:"))
        if take=='y':
            take_card(Player_hand)
            print_player_cards(Player_hand)
            print_dealer_cards(Dealer_hand, False)
        else:
            taking_card=False
    if card_score(Player_hand)<=21:
        while card_score(Dealer_hand) < 17:
            take_card(Dealer_hand)


    print(f"Your Final cards : {Player_hand}  Your final Score: {card_score(Player_hand)}")
    print_dealer_cards(Dealer_hand,True)
    if (card_score(Player_hand)<card_score(Dealer_hand)) or card_score(Player_hand)>21:
        print("You Lose :'') ")
    elif (card_score(Player_hand)>card_score(Dealer_hand)) or card_score(Dealer_hand)>21:
        print("You Win XD")
    elif (card_score(Player_hand)==card_score(Dealer_hand)):
        print(" its Drawww")
    start_game = input("Want to start playing BlackJack? Type 'y' to start : ")