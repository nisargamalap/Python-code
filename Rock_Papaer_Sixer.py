import random
def main():
  """
  Plays a game of Rock, Paper, Sixer against the computer.
  """
  # Define the possible choices for the player and computer.
  choices = ["Rock", "Paper", "Sixer"]

  # Get the player's choice.
  player_choice = input("Choose Rock, Paper, or Sixer: ").capitalize()

  # Make sure the player's choice is valid.
  if player_choice not in choices:
    print("Invalid choice. Please choose Rock, Paper, or Sixer.")
    return

  # Choose the computer's choice randomly.
  computer_choice = random.choice(choices)

  # Print the player's and computer's choices.
  print("You chose:", player_choice)
  print("Computer chose:", computer_choice)

  # Determine the winner.
  if player_choice == computer_choice:
    print("It's a tie!")
  elif player_choice == "Rock":
    if computer_choice == "Sixer":
      print("Sixer crushes Rock! You lose.")
    else:
      print("Rock smashes Scissors! You win!")
  elif player_choice == "Paper":
    if computer_choice == "Rock":
      print("Paper covers Rock! You win!")
    else:
      print("Sixer cuts Paper! You lose.")
  elif player_choice == "Sixer":
    if computer_choice == "Paper":
      print("Sixer cuts Paper! You win!")
    else:
      print("Rock crushes Sixer! You lose.")

if __name__ == "__main__":
  main()