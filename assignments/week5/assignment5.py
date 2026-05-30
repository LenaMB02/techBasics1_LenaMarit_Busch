import time

# GLOBAL CONSTANTS
MIN_TRAINING = 10
MAX_TRAINING = 60


# FUNCTIONS

def welcome():
    """Welcomes the player and asks for their name."""
    print("--- ⚽\t Welcome to the sports test \t---")
    time.sleep(1)
    player_name = input("What's your name? ")
    print(f"Hello, {player_name}, let's train.")
    time.sleep(1)
    return player_name


def choose_sport():
    """Asks the user for their preferred sport (ignores upper/lowercase and spaces)."""
    # .strip() removes accidental leading/trailing spaces, .lower() converts it entirely to lowercase
    choice = input("Which sport do you prefer? Football or Tennis: ").strip().lower()

    if choice == "football":
        print("Perfect, let's go to the soccer field!⚽")
    elif choice == "tennis":
        print("Go, take your racket!🎾")
    else:
        print("That's nice as well, movement is always good!")

    time.sleep(1)
    return choice


def get_duration():
    """Returns the validated training duration."""
    duration = 0
    while duration < MIN_TRAINING or duration > MAX_TRAINING:
        duration_input = input(f"How many minutes do you want to train? ({MIN_TRAINING}-{MAX_TRAINING}): ")
        duration = int(duration_input)

        if duration < MIN_TRAINING or duration > MAX_TRAINING:
            print(f"This is not a good training. Choose a time between {MIN_TRAINING} and {MAX_TRAINING}!")
            time.sleep(1)

    if duration > 30:
        print("Wow, you are very fit!💪")
    else:
        print("A short and sweet training!🦦")
    time.sleep(1)
    return duration


def training_finale(sport_type):
    """Executes the sport-specific final questions based on lowercase inputs."""
    if sport_type == "football":
        afterwards = input("Do you want to go for a walk or shower afterwards? ").strip().lower()
        if afterwards == "go for a walk" or afterwards == "walk":
            print("You have so much energy!")
        else:
            print("Relax and take a break after your training!")

    elif sport_type == "tennis":
        hit = input("Do you want to train your forehand or backhand? ").strip().lower()
        if hit == "forehand":
            print("Your forehand will improve so fast!")
        else:
            print("Nice choice, the backhand is very important!")

    time.sleep(1)


# MAIN EXECUTION
if __name__ == "__main__":
    name = welcome()
    sport = choose_sport()
    duration = get_duration()
    training_finale(sport)

    # A 2-second pause
    time.sleep(2)

    print(f"--- 🎾⚽ Sports test done. See you next time, {name}! ⚽🎾 ---")