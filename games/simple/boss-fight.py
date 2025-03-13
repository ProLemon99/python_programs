import random
import time
import os

# Sleep function for better pacing
def sleep(duration=1):
    time.sleep(duration)

# Clear screen function for readability
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Difficulty settings
def choose_difficulty():
    while True:
        clear_screen()
        print("=== Choose Difficulty ===")
        print("[1] Easy  - (More HP, Weaker Boss)")
        print("[2] Medium - (Balanced)")
        print("[3] Hard  - (Less HP, Stronger Boss)")

        choice = input("\nEnter 1, 2, or 3: ").strip()
        
        if choice == "1":
            return 40, 50  # Player HP, Boss HP
        elif choice == "2":
            return 30, 55
        elif choice == "3":
            return 25, 65
        else:
            print("\nInvalid choice. Try again.")
            sleep(1)

# Game introduction
clear_screen()
print("=== Welcome to the Boss Fight Game! ===")
sleep(2)

# Set player and boss health based on difficulty
player_hp, boss_hp = choose_difficulty()
max_hp = player_hp
boss_max_hp = boss_hp

# Game loop
play = True
while play:
    clear_screen()
    print(f"Your Health: {player_hp}/{max_hp}")
    print(f"Boss Health: {boss_hp}/{boss_max_hp}\n")
    print("[A] Attack  |  [D] Defend  |  [H] Heal")
    
    # Player's Turn
    player_action = input("\nChoose your action: ").strip().upper()
    
    if player_action == "A":  # Attack
        clear_screen()
        damage = random.randint(5, 12)
        crit_chance = random.randint(1, 10)
        if crit_chance == 10:  # 10% chance to deal critical hit
            damage *= 2
            print("CRITICAL HIT!!")
        print(f"You attack the boss for {damage} damage!")
        boss_hp -= damage

    elif player_action == "D":  # Defend
        clear_screen()
        print("You brace for impact, reducing damage next turn.")

    elif player_action == "H":  # Heal
        heal_amount = random.randint(8, 15)
        player_hp += heal_amount
        if player_hp > max_hp:
            player_hp = max_hp
        clear_screen()
        print(f"You heal for {heal_amount} HP!")
    else:
        print("Invalid input! Choose A, D, or H.")
        sleep(1)
        continue

    sleep(1)

    # Boss's Turn (if still alive)
    if boss_hp > 0:
        boss_action = random.randint(1, 6)

        if boss_action <= 4:  # Attack (66% chance)
            boss_damage = random.randint(4, 10)
            if player_action == "D":  # Reduce damage if player defended
                boss_damage = max(1, boss_damage - random.randint(2, 6))
                print("You block some of the damage!")
            print(f"The boss attacks you for {boss_damage} damage!")
            player_hp -= boss_damage

        elif boss_action == 5:  # Defend (16% chance)
            print("The boss prepares to block your next attack!")

        else:  # Heal (16% chance)
            boss_heal = random.randint(5, 10)
            boss_hp += boss_heal
            if boss_hp > boss_max_hp:
                boss_hp = boss_max_hp
            print(f"The boss regenerates {boss_heal} HP!")

        sleep(1)

    # Check for win/lose conditions
    if boss_hp <= 0:
        clear_screen()
        print("You defeated the boss! Congratulations!")
        break
    elif player_hp <= 0:
        clear_screen()
        print("You have been defeated... Good luck next time!")
        break

# End of game
print("\nThanks for playing!")