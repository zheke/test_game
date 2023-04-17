import random

# Define island items and enemies
island_items = ["rocks", "sticks", "berries"]
enemies = ["raiders", "cannibals", "wild animals", "neutral"]
survivors = ["friendly", "neutral"]

# Define player objectives
objectives = {
    "Discover your identity": False,
    "Find a way off the island": False,
    "Survive until rescue arrives": False,
    "Find out the state of the world": False
}

# Define player attributes
health = 100
hunger = 0
thirst = 0

# Define helper functions
def print_status():
    print("Health:", health)
    print("Hunger:", hunger)
    print("Thirst:", thirst)
    print("Island items:", island_items)
    print("Objectives:")
    for objective, completed in objectives.items():
        print(f"- {objective}: {'Completed' if completed else 'Not completed'}")

def get_player_choice(choices):
    while True:
        print("What would you like to do?")
        for i, choice in enumerate(choices):
            print(f"{i + 1}. {choice}")
        try:
            choice = int(input()) - 1
            if 0 <= choice < len(choices):
                return choices[choice]
        except ValueError:
            pass
        print("Invalid choice. Please try again.")

# Game start
print("You wake up on a deserted island with amnesia.")
print("You don't remember who you are or how you got here.")
print("You need to find a way off the island and discover your identity.")
print("You also need to survive until rescue arrives and find out the state of the world.")
print("Good luck!")
print()

# Main game loop
while True:

    # Print player status and get player choice
    print_status()
    choices = ["Explore the island", "Rest and recover", "Check inventory", "Quit game"]
    choice = get_player_choice(choices)

    # Handle player choice
    if choice == "Explore the island":

        # Randomly encounter an enemy or neutral survivor
        enemy = random.choice(enemies)

        # Handle raiders
        if enemy == "raiders":
            print("The raiders attack you.")
            health -= 30
            if health <= 0:
                print("You died.")
                break
            else:
                print("You fight back and defeat them.")
                island_items.append("gun")

        # Handle cannibals
        elif enemy == "cannibals":
            print("The cannibals attack you.")
            health -= 40
            if health <= 0:
                print("You died.")
                break
            else:
                print("You run away and hide.")
                print("You find an old mine while you're running and accidentally step on it.")
                print("You lose consciousness.")
                print("When you wake up, you have a flashback and remember your name.")
                objectives["Discover your identity"] = True

        # Handle wild animals
        elif enemy == "wild animals":
            print("The wild animals attack you.")
            print("You fight back and defeat them.")
            print("You find some clues that suggest the rest of the world might not be okay.")
            objectives["Find out the state of the world"] = True

        # Handle neutral survivors
        elif enemy == "neutral":
            survivor = random.choice(survivors)
            if survivor == "friendly":
                print("You encounter a friendly survivor.")
                print("They give you some food and water.")
                island_items.append("food")
                island_items.append("water")
            else:
                print("You encounter a neutral survivor.")
                print("They don't seem interested in talking to you.")
        # Decrease hunger and thirst
        hunger += 10
        thirst += 10

    elif choice == "Rest and recover":
        # Increase health and decrease hunger and thirst
        health += 20
        hunger -= 10
        thirst -= 10

        # Make sure health, hunger, and thirst don't go over 100 or under 0
        health = max(min(health, 100), 0)
        hunger = max(min(hunger, 100), 0)
        thirst = max(min(thirst, 100), 0)

    elif choice == "Check inventory":
        print("You have the following items in your inventory:")
        print(", ".join(island_items))

    elif choice == "Quit game":
        break

# Check if player completed all objectives
    if all(objectives.values()):
        print("Congratulations! You have completed all objectives and won the game.")
        break
