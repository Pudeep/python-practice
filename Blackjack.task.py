import random
from art import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_score(u_score, c_score):
    if u_score == c_score:
        return "draw"
    elif c_score == 0:
        return "opponent has blackjack. You lose!"
    elif u_score == 0:
        return "You win with a blackjack"
    elif u_score > 21:
        return "You went over. You lose!"
    elif c_score > 21:
        return "Opponent went over. you win!"
    elif u_score > c_score:
        return "You win!"
    else:
        return "you lose!"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, Total score: {user_score}")
        print(f"Computer first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            draw_card = input("Type 'y' to continue or 'n' to stop. ")
            if draw_card == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, Total score: {user_score}")
    print(f"Computer final hand: {computer_cards}, Total score: {computer_score}")
    print(compare_score(user_score, computer_score))

while input("Do you want to play a game of Blackjack? (y/n) ").lower() == "y":
    print("\n" * 20)
    play_game()



















