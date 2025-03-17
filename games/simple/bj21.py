import random

def rules():
    print("\n***********************")
    print("* Blackjack / 21 Rules *")
    print("***********************")
    print("\nObjective:")
    print("The goal of Blackjack is to have a hand value closer to 21 than the dealer's hand, without exceeding 21.")
    print("\nCard Values:")
    print("- Number cards (2 through 10) are worth their face value.")
    print("- Face cards (Jack, Queen, King) are each worth 10 points.")
    print("- Aces can be worth 1 or 11 points, depending on which value benefits the hand more.")
    print("\nGameplay:")
    print("1. Each player, including the dealer, is dealt two cards.")
    print("2. Players are allowed to 'hit' (take another card) or 'stand' (keep their current hand).")
    print("3. Players can continue to hit until they decide to stand or until their hand exceeds 21, resulting in a 'bust' and an automatic loss.")
    print("4. After all players have completed their turn, the dealer reveals their face-down card.")
    print("5. The dealer must hit until their hand reaches at least 17. ")
    print("6. If the dealer busts, all remaining players win.")
    print("7. If the dealer doesn't bust, the player's hands are compared to the dealer's hand.")
    print("8. The player wins if their hand is closer to 21 than the dealer's without busting.\n")

def ace(a):
    """If first element is 'A' it converts it into 11\n
    and if any other element is 'A' it converts it into '1' or '11' based on sum of list such that sum<=21
    """
    for i in a:
        if a[0] == "A":
            a[0] = 11

        elif i == "A" and a[0] != "A":
            if sum(a[:-1]) > 10:
                a[-1] = 1
            else:
                a[-1] = 11

def test(a):
    """Checks if the sum of elements in the list is greater than 21 or not\n
    if sum > 21, returns 'False',\n
    else returns 'True
    """
    if sum(a) > 21:
        return False
    else:
        return True

def blackjack(user_list, computer_list):
    ace(user_list)
    user_sum = sum(user_list)
    print(f"\nYou have {user_list}. sum = {user_sum}")

    ace(computer_list)
    print(f"Dealer has {computer_list} and one mystery card, sum = ?")

    hit_status = True
    while hit_status:
        user_next_move = input("Would you like to hit(h) or stand(s)?:\n->>").lower()
        if user_next_move == 'h':
            user_list.append(random.choice(list))
            ace(user_list)
            if test(user_list):
                print(f"You have {user_list}. sum = {sum(user_list)}")
            elif not test(user_list):
                print(f"Busts!! You have {user_list}. sum = {sum(user_list)} \n ***** You have lost :(")
                return
        elif user_next_move == 's':
            print(f"You have {user_list}. sum = {sum(user_list)}")
            hit_status = False
        else:
            print("Wrong input")
            return

    if sum(user_list) == 21:
        print(f"You have sum = {sum(user_list)} and dealer has sum = {sum(computer_list)} \n ***** You have won!!")

    while sum(computer_list) <= 17:
        computer_list.append(random.choice(list))
        ace(computer_list)
    if test(computer_list):
        print(f"dealer has {computer_list}. sum = {sum(computer_list)}")
    else:
        print(f"Busts!! dealer has {computer_list}. sum = {sum(computer_list)} \n ***** You have won!!")
        return

    if sum(user_list) > sum(computer_list):
        print(f"You have sum = {sum(user_list)} and dealer has sum = {sum(computer_list)} \n ***** You have won!!")
    elif sum(user_list) < sum(computer_list):
        print(f"You have sum = {sum(user_list)} and dealer has sum = {sum(computer_list)} \n ***** You have lost :(")
    else:
        print(f"You have sum = {sum(user_list)} and dealer has sum = {sum(computer_list)} \n ***** You have drawn :|")

# Main
list = (2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, "A")
print("\n**********\nWelcome to Blackjack / 21")

while True:
    if  input("Enter 's' to start or 'q' to quit\n->>")== "s":
        if input("Do you wish to see the rules? (y/n)\n->>").lower() == "y":
            rules()
        user_list = [random.randint(2, 10), random.choice(list)]
        computer_list = [random.choice(list)]

        blackjack(user_list = user_list, computer_list = computer_list)
    else:
        break