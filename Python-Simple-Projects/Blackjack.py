import random

# Card deck (values only)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    """Return a random card from the deck."""
    return random.choice(cards)


def calculate_score(hand):
    """Calculate score of a hand."""
    score = sum(hand)

    # Check for Blackjack (Ace + 10)
    if score == 21 and len(hand) == 2:
        return 0  # 0 represents Blackjack

    # Adjust Ace from 11 to 1 if score > 21
    while 11 in hand and score > 21:
        hand.remove(11)
        hand.append(1)
        score = sum(hand)

    return score


def compare(user_score, dealer_score):
    """Compare scores and return result message."""

    if user_score == dealer_score:
        return "Draw 🙃"
    elif dealer_score == 0:
        return "You lose, dealer has Blackjack 😱"
    elif user_score == 0:
        return "You win with Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif dealer_score > 21:
        return "Dealer went over. You win 😁"
    elif user_score > dealer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    print("\n🃏 Welcome to Blackjack!")

    user_hand = []
    dealer_hand = []

    # Initial deal
    for _ in range(2):
        user_hand.append(deal_card())
        dealer_hand.append(deal_card())

    game_over = False

    while not game_over:
        user_score = calculate_score(user_hand)
        dealer_score = calculate_score(dealer_hand)

        print(f"\nYour cards: {user_hand}, current score: {user_score}")
        print(f"Dealer's first card: {dealer_hand[0]}")

        # Check for Blackjack or bust
        if user_score == 0 or dealer_score == 0 or user_score > 21:
            game_over = True
        else:
            should_hit = input("Type 'y' to get another card, 'n' to pass: ").lower()
            if should_hit == "y":
                user_hand.append(deal_card())
            else:
                game_over = True

    # Dealer plays
    while dealer_score != 0 and dealer_score < 17:
        dealer_hand.append(deal_card())
        dealer_score = calculate_score(dealer_hand)

    print(f"\nYour final hand: {user_hand}, final score: {user_score}")
    print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}")

    print(compare(user_score, dealer_score))


# Game loop
while input("\nPlay Blackjack? Type 'y' or 'n': ").lower() == "y":
    play_game()