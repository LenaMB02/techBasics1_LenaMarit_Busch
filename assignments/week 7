import csv
import sys
import random
from datetime import datetime

# debug flag
# true = skips the main game loop and tests leaderboard saving system
# false = activates the normal game mode
DEBUG = True

# counts every action/command as their final score (the lower the better)
turns_counter = 0

# --- Game State ---

inventory = []
# added tennis items here. Total length is 6 (1 more than max inventory size (5)
items_in_room = [
    {"name": "Racket", "type": "equipment", "description": "A brand new Head tennis racket."},
    {"name": "tennisballs", "type": "equipment", "description": "A can of 4 tennis balls."},
    {"name": "Card", "type": "tool", "description": "Your credit card to pay at the checkout."},
    {"name": "Grip", "type": "accessory", "description": "White overgrip tape for the handle."},
    {"name": "Water", "type": "food", "description": "A cold bottle of water for hydration."},
    {"name": "Cap", "type": "accessory", "description": "A white cap against the sun."}
]
MAX_INVENTORY_SIZE = 5

# --- Functions ---

def show_inventory():
    # list of all names (items) in the inventory, considering the case when the list is empty
    if len(inventory) == 0:
        print("Your cart is empty")
    else:
        print("Your cart (" + str(len(inventory)) + "/" + str(MAX_INVENTORY_SIZE) + ")")
        for item in inventory:
            print("- " + item["name"])

def show_room_items():
    # list all items available in the shop
    if len(items_in_room) == 0:
        print("The shop is completely empty.")
    else:
        print("Items available in the shop:")
        for item in items_in_room:
            print("- " + item["name"] + " (" + item["type"] + ")")

def pick_up(item_name):
    # check if the player has reached max inventory size limit
    if len(inventory) >= MAX_INVENTORY_SIZE:
        print("Your cart is full! Drop something first.")
        return

    for item in items_in_room:
        if item["name"].lower() == item_name.lower():
            inventory.append(item)
            items_in_room.remove(item)
            print("You added " + item["name"] + " to your cart.")
            return

    print("That item is not in the shop.")

def drop(item_name):
    for item in inventory:
        if item["name"].lower() == item_name.lower():
            inventory.remove(item)
            items_in_room.append(item)
            print("You removed " + item["name"] + " from your cart.")
            return

    print("You don't have that item in your cart.")

def use(item_name):
    # using the item differently depends on the type
    # scenario goal: using the card to buy racket and tennisballs
    if item_name.lower() == "card":
        has_racket = False
        has_tennisballs = False

        # scan the inventory to check if both required items are in the cart
        for item in inventory:
            if item["name"].lower() == "racket":
                has_racket = True
            if item["name"].lower() == "tennisballs":
                has_tennisballs = True

        # check if win conditions are met (racket and tennisballs have to be in the cart)
        if has_racket and has_tennisballs:
            print("\n*** GAME OVER - YOU WIN! ***")
            print("You successfully paid for your tennis gear. See you on the court!")
            end_game_and_save(turns_counter)
        else:
            print("You cannot checkout yet. You need at least the Racket and tennisballs in your cart.")

    elif item_name.lower() == "water":
        print("You drink the water. Refreshing!")
        # optional: removing it from inventory if consumed (drank)
        for item in inventory:
            if item["name"].lower() == "water":
                inventory.remove(item)
                break
    else:
        print("You cannot use this item right now.")


def examine(item_name):
    # you can only examine an item if it's in your inventory or if it's in the room
    # using .get() to avoid mistake
    for item in inventory + items_in_room:
        if item["name"].lower() == item_name.lower():
            print("[" + item["name"] + "]: " + item.get("description", "No description available."))
            return
    print("You cannot see that item anywhere")

# record saving (leaderboard) system
def end_game_and_save(final_score):
    print("Your final score is " + str(final_score))
    user_name = input("Enter your name: ").strip()
    if user_name == "":
        user_name = "Anonymous player"

    # generate current timestamp string
    timestamp = datetime.now().strftime("%m/%d/%Y %H:%M:%S")

    # create new record row as list of strings
    new_record = [user_name, timestamp, str(final_score)]
    all_records = []

    # 1. Read existing file data using Try-Except for error handling
    try:
        with open('tennis_records.csv', 'r', newline='', encoding='utf-8') as file:
            csvreader = csv.reader(file)
            header = next(csvreader)  # skips the first row (the column titles)

            for row in csvreader:
                if row:  # prevents errors caused by empty rows
                    all_records.append(row)
    except FileNotFoundError:
        # if the file does not exist yet (first play), handle error gracefully by keeping a fresh list
        all_records = []

    # add the current gameplay data to the master list
    all_records.append(new_record)

    # 2. Simple sorting helper function
    def get_score(row):
        return int(row[2])  # converts it to a number

    # sort the master record list based on the helper function values (lowest action count comes first)
    all_records.sort(key=get_score)

    # 3. Write all combined records back to the CSV file
    with open('tennis_records.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Timestamp", "Score"])  # write column header titles first

        for record in all_records:
            writer.writerow(record)

    # 4. Display the simple Leaderboard layout in the terminal
    print("\n--- LEADERBOARD ---")
    counter = 1
    for record in all_records:
        if counter > 5:  # cap the leaderboard display to only show the top 5 players
            break
        print(str(counter) + ". " + record[0] + " - " + record[1] + " - Actions: " + record[2])
        counter += 1

    sys.exit()

# --- Game Loop ---

def game_loop():
    global turns_counter

    if DEBUG:
        print("--- DEBUG MODE ACTIVE ---")
        print("skipping main game body. Triggering instant placeholder save...")
        placeholder_score = random.randint(5, 15) # creates a simulated test score
        end_game_and_save(placeholder_score) # jumps to the saving system
        return  # exits the loop immediately

    # print welcome messages and state the win scenario to the player
    print("Welcome to the Tennis Shop Game!")
    print("Goal: Get a Racket, Tennisballs, and use your card to checkout.")
    print("Type 'help' for a list of commands.")

    # infinite loop to keep the game running until the player wins or quits the game
    while True:
        command = input("\n> ").strip().lower()

        turns_counter += 1

        match command.split():
            case ["help"]:
                print("Commands: inventory, look, pickup [item], drop [item], use [item], examine [item], quit")
            case ["inventory"]:
                show_inventory()
            case ["look"]:
                show_room_items()
            case ["pickup", item_name]:
                pick_up(item_name)
            case ["drop", item_name]:
                drop(item_name)
            case ["use", item_name]:
                use(item_name)
            case ["examine", item_name]:
                examine(item_name)
            case ["quit"]:
                print("Thanks for playing!")
                break
            case _: # else
                print("Unknown command. Type 'help' to see available commands.")

if __name__ == "__main__":
    game_loop()
