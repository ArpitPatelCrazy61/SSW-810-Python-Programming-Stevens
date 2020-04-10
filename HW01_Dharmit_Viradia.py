from random import choice

def get_human_move() -> str:
    """ Ask the user for R, P or S or Rock, Paper or Scissors.  Loop until given a valid input """
    while True:
        user_input: str = input("Please Enter 'R for Rock or Rock', 'P for Paper or Paper', 'S for Scissors or Scissors' or 'Q or Quit to quit': ").lower()
        

        if (user_input == "r" or user_input == "rock"):
            return "rock"

        elif (user_input == "p" or user_input == "paper"):
            return "paper"

        elif (user_input == "s" or user_input == "scissors"):
            return "scissors"

        elif (user_input == "q" or user_input == "quit"):
            return "quit"

        else:
            return "error"
    

def get_computer_move() -> str:
    """ return the computer's random choice using random.choice """

    move: str = choice(['rock', 'paper', 'scissors'])
    return move  
        
def play_game() -> bool:
    """ play Rock/Paper/Scissors
        The human may enter 'Q' or 'q' any time to stop the game.
        Get the human's move, the computer's move, and print a message with the winner.
        Return a bool to specify if the human wants to play again, 
        i.e. False when the human wants to quit or True to play again
    """
    human: str = get_human_move()
    if human == 'quit':  # human wants to quit
        return False

    computer: str = get_computer_move()
    if human == computer:
        print("Its a Tie")
    
    elif human == "rock":
        if computer == "paper":
            print("You Loose")
        else:
            print("You Win")

    elif human == "paper":
        if computer == "scissors":
            print("You Loose")
        else:
            print("You Win")

    elif human == "scissors":
        if computer == "rock":
            print("You Loose")
        else:
            print("You Win")

    elif human == "error":
        print("Please Enter a Valid Option")

    return True  # play again

def main() -> None:
    """ Play multiple games until the human asks to stop """
    again: bool = True
    while again:
        again = play_game()
        
    print("Thanks for playing!")

if __name__ == "__main__":
    main()