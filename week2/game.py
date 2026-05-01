import time

# Welcome-effect (short hello)
print("--- ⚽🎾️Welcome to the sports test 🎾⚽️ ---")
time.sleep(1)

# 1. User Input: name
name = input("What's your name?")
print("Hello,", name, ", let's train.")
time.sleep(1)

# 2. User Input: choice of sport
sport = input("Which sport do you prefer? Football or Tennis:")

if sport == "Football":
    print("Perfect, let's go to the soccer field!⚽️")
    time.sleep(1)

elif sport == "Tennis":
    print("Go, take your racket!🎾")
    time.sleep(1)

else:
    print("That's nice as well, movement is always good!")
    time.sleep(1)

# 3. User Input: duration of training
duration = 0
while duration < 10 or duration > 60:
    duration_input = input("how many minutes do you want to train?(10-60): ")
    duration = int(duration_input)

    if duration < 10 or duration > 60:
        print("This is not a good training. Choose a time between 10 and 60!")
        time.sleep(1)

if duration > 30:
        print("Wow, you are very fit!💪🏼")
        time.sleep(1)
else:
        print("A short and sweet training!🦦")
        time.sleep(1)

# 4. Conditional based on sport and duration
if sport == "Football":
        afterwards = input("Do you want to go for a walk or shower afterwards?")
        if afterwards == "go for a walk":
            print("You have so much energy!")
        else:
            print("Relax and teak a break after your training!")
            time.sleep(1)

elif sport == "Tennis":
    # another conditional for tennis
    hit = input("Do you want to train your forehand or backhand?")
    if hit == "forehand":
        print("Your forehand will improve so fast!")
    else:
        print("Nice choice, the backhand is very important!")
        time.sleep(1)

time.sleep(1)
print("--- 🎾⚽️ Sports test done. See you next time,", name, "! ⚽️🎾 ---")