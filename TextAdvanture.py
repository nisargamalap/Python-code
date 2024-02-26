def start_game():
    print("Welcome to the Text Adventure Game!")
    print("You find yourself in a dark room. What do you do?")
    print("1. Look for a light switch")
    print("2. Feel around the walls")
    print("3. Wait for something to happen")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        option_light_switch()
    elif choice == "2":
        option_feel_walls()
    elif choice == "3":
        option_wait()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        start_game()

def option_light_switch():
    print("You flick the light switch and the room lights up.")
    print("You see a door on the left and a window on the right.")
    print("What do you do next?")
    print("1. Open the door")
    print("2. Look out the window")
    print("3. Explore the room")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        print("You open the door and escape. Congratulations, you win!")
    elif choice == "2":
        print("You look out the window and see nothing but darkness.")
        print("You turn around and decide to explore the room.")
        option_explore_room()
    elif choice == "3":
        option_explore_room()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        option_light_switch()

def option_feel_walls():
    print("You feel around the walls but find nothing of interest.")
    print("Suddenly, you hear a noise coming from behind you.")
    print("What do you do?")
    print("1. Investigate the noise")
    print("2. Ignore it and continue feeling the walls")
    print("3. Run away")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        print("You investigate the noise and find a hidden passage.")
        print("You enter the passage and escape. Congratulations, you win!")
    elif choice == "2":
        print("You ignore the noise and continue feeling the walls.")
        print("Unfortunately, you find nothing useful and remain trapped.")
        print("Game over.")
    elif choice == "3":
        print("You panic and run blindly into the darkness.")
        print("You trip and fall, unable to escape. Game over.")
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        option_feel_walls()

def option_wait():
    print("You wait for something to happen, but nothing does.")
    print("You realize that you must take action to escape.")
    start_game()

def option_explore_room():
    print("You explore the room and find a key hidden under a chair.")
    print("You pick up the key and decide to...")
    print("1. Open the door with the key")
    print("2. Look for another way out")

    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        print("You use the key to open the door and escape. Congratulations, you win!")
    elif choice == "2":
        print("You search the room for another way out but find none.")
        print("You decide to use the key to open the door instead.")
        print("You escape. Congratulations, you win!")
    else:
        print("Invalid choice. Please enter 1 or 2.")
        option_explore_room()

# Start the game
start_game()