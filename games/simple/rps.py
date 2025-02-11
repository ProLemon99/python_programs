import random

def play():
    while True:
        user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors, or 'q' to quit\n")
        if user == 'q':
            print("Thanks for playing!")
            break
        
        if user not in ['r', 'p', 's']:
            print("Invalid choice. Please choose 'r', 'p', 's', or 'q' to quit.")
            continue
        
        computer = random.choice(['r', 'p', 's'])
        print(f"Computer chose: {computer}")

        if user == computer:
            print("It's a tie!")
        elif is_win(user, computer):
            print("You won!")
        else:
            print("You lost!")

def is_win(player, opponent):
    # return True if player wins
    # r > s, s > p, p > r
    return (player == 'r' and opponent == 's') or \
           (player == 's' and opponent == 'p') or \
           (player == 'p' and opponent == 'r')

play()