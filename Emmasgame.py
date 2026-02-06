

inventory = []

def welcome_player():
    print("Welcome to the Adventure Game!")
    print("Your journey begins here...")
    player_name = input("What is your name, adventurer?")
    
    print(f"Welcome, {player_name}! Your journey begins now.")

    return player_name

def describe_area():
    starting_area = """
    You find yourself in a dark forest.
        You see two paths ahead:
        1. Take hte left path into the dark woods
        2. Take the right path toward the mountain pass
        3. Stay where you are
        Type "i" to view your inventory.
        """
    print(starting_area)

player_name = welcome_player()
describe_area();

def add_to_inventory(item):
    inventory.append(item)
    print(f"A {item} was added to your inventory")

decision = input("Do you wish to take the path? 1, 2, 3, or i:").lower()

if decision == "1":
    print(f"{player_name}! You step into the dark woods.")
    add_to_inventory("lantern")
elif decision == "2":
    print(f"{player_name}! You step into the mountain pass.")
    add_to_inventory("map")
elif decision == "3":
    print(f"{player_name}! You don't go anwhere.")
elif decision == "i":
    print(f"{player_name}! This is your inventory.")
else:
    print("Confused, you stand still, unsure of what to do.")

