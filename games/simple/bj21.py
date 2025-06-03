# Currently kind of bugged but still somewhat playable

import random

# Global flag to track if rules were declined
rules_declined = False

def rules():
    """Display the game rules"""
    print("\n" + "-" * 25)
    print("*    Blackjack / 21 Rules    *")
    print("-" * 25)
    print("\nObjective:")
    print("The goal is to have a hand value closer to 21 than the dealer's hand,")
    print("without exceeding 21.")
    
    print("\nCard Values:")
    print("- Number cards (2-10): Face value")
    print("- Face cards (J, Q, K): 10 points")
    print("- Aces: 1 or 11 points (whichever benefits the hand)")
    
    print("\nGameplay:")
    print("1. Each player gets two cards (dealer has one hidden)")
    print("2. Hit (take another card) or Stand (keep current hand)")
    print("3. Continue hitting until you Stand or Bust (>21)")
    print("4. Dealer reveals cards and hits until reaching 17+")
    print("5. Closest to 21 without busting wins\n")

def ace(hand):
    """Adjust Ace values in the hand"""
    for i, card in enumerate(hand):
        if i == 0 and card == "A":
            hand[0] = 11
        elif card == "A" and hand[0] != "A":
            hand[-1] = 1 if sum(hand[:-1]) > 10 else 11

def is_valid_hand(hand):
    """Check if hand value is <= 21"""
    return sum(hand) <= 21

def blackjack(user_hand, dealer_hand):
    """Main game logic"""
    # Initial deal
    ace(user_hand)
    user_sum = sum(user_hand)
    print(f"\nYou have {user_hand}. Sum = {user_sum}")
    ace(dealer_hand)
    print(f"Dealer has {dealer_hand} and one mystery card")

    # Player turn
    while True:
        choice = input("Hit (h) or Stand (s)?\n-> ").lower()
        if choice == 'h':
            user_hand.append(random.choice(cards))
            ace(user_hand)
            if is_valid_hand(user_hand):
                print(f"You have {user_hand}. Sum = {sum(user_hand)}")
            else:
                print(f"Bust! {user_hand}. Sum = {sum(user_hand)}\nYou lose!")
                return
        elif choice == 's':
            print(f"You stand with {sum(user_hand)}")
            break
        else:
            print("Invalid input")
            return

    # Dealer turn
    while sum(dealer_hand) <= 17:
        dealer_hand.append(random.choice(cards))
        ace(dealer_hand)
    
    print(f"\nDealer has {dealer_hand}. Sum = {sum(dealer_hand)}")
    
    # Determine winner
    user_sum = sum(user_hand)
    dealer_sum = sum(dealer_hand)
    
    if not is_valid_hand(dealer_hand):
        print("Dealer busts! You win!")
    elif user_sum > dealer_sum:
        print(f"You win! {user_sum} vs {dealer_sum}")
    elif user_sum < dealer_sum:
        print(f"You lose! {user_sum} vs {dealer_sum}")
    else:
        print(f"Push! {user_sum} vs {dealer_sum}")

# Game setup
cards = (2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, "A")
print("Welcome to Blackjack 21!")

# Main game loop
while True:
    choice = input("\nStart (s) or Quit (q)?\n-> ").lower()
    if choice == "s":
        # Only offer rules if they were never declined before
        if not rules_declined:
            see_rules = input("See rules? (y/n)\n-> ").lower()
            if see_rules == "y":
                rules()
            else:
                rules_declined = True  # Player declined, don't ask again
        user_hand = [random.choice(cards), random.choice(cards)]
        dealer_hand = [random.choice(cards)]
        blackjack(user_hand, dealer_hand)
    elif choice == "q":
        break
    else:
        print("Invalid input")