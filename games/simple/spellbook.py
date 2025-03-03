import requests
import random

# API Base URL
API_URL = "https://www.dnd5eapi.co/api/spells/"

# Dictionary to store spells
spellbook = {}

# Player and enemy stats
player = {"health": 100, "mana": 50}
enemy = {"health": 100}

def search_spell(spell_name):
    """Search for a spell in the D&D API and return its details."""
    response = requests.get(API_URL + spell_name.lower().replace(" ", "-"))
    if response.status_code == 200:
        spell_data = response.json()
        return {
            "name": spell_data["name"],
            "level": spell_data["level"],
            "description": spell_data["desc"][0],  # First part of the description
            "damage": random.randint(5, 20)  # Random damage for simplicity
        }
    else:
        print("Spell not found.")
        return None

def add_spell_to_spellbook(spell_name):
    """Add a spell to the spellbook if found."""
    spell = search_spell(spell_name)
    if spell:
        spellbook[spell_name] = spell
        print(f"Added {spell_name} to your spellbook!")

def view_spellbook():
    """Display all stored spells."""
    if not spellbook:
        print("Your spellbook is empty.")
    else:
        for spell in spellbook.values():
            print(f"{spell['name']} (Level {spell['level']}): {spell['description']} - Damage: {spell['damage']}")

def cast_spell(spell_name):
    """Cast a spell from the spellbook."""
    if spell_name in spellbook:
        spell = spellbook[spell_name]
        if player["mana"] >= spell["level"] * 2:
            player["mana"] -= spell["level"] * 2
            damage = spell["damage"]
            enemy["health"] -= damage
            print(f"You cast {spell_name} and dealt {damage} damage to the enemy!")
        else:
            print("Not enough mana to cast this spell.")
    else:
        print("You don't know that spell.")

def enemy_attack():
    """Enemy attacks the player."""
    damage = random.randint(5, 15)
    player["health"] -= damage
    print(f"The enemy attacks you and deals {damage} damage!")

def combat():
    """Combat loop."""
    while player["health"] > 0 and enemy["health"] > 0:
        print(f"\nPlayer Health: {player['health']} | Mana: {player['mana']}")
        print(f"Enemy Health: {enemy['health']}")
        print("1. Cast Spell")
        print("2. Flee")
        choice = input("Choose an action: ")

        if choice == "1":
            spell_name = input("Enter the spell name: ")
            cast_spell(spell_name)
            if enemy["health"] > 0:
                enemy_attack()
        elif choice == "2":
            print("You fled from the battle!")
            break
        else:
            print("Invalid choice. Please try again.")

    if player["health"] <= 0:
        print("You have been defeated!")
    elif enemy["health"] <= 0:
        print("You have defeated the enemy!")

def main():
    while True:
        print("\nSpellbook Game Menu:")
        print("1. Search for a Spell")
        print("2. Add Spell to Spellbook")
        print("3. View Spellbook")
        print("4. Enter Combat")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            spell_name = input("Enter the spell name: ")
            spell = search_spell(spell_name)
            if spell:
                print(f"{spell['name']} (Level {spell['level']}): {spell['description']} - Damage: {spell['damage']}")
        elif choice == "2":
            spell_name = input("Enter the spell name to add: ")
            add_spell_to_spellbook(spell_name)
        elif choice == "3":
            view_spellbook()
        elif choice == "4":
            print("A wild enemy appears!")
            combat()
        elif choice == "5":
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()