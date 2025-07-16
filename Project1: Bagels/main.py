# === BAGELS GAME PLAN ===

# 1. Setup Phase
# - Define number of digits (e.g., 3)
# - Define maximum number of guesses (e.g., 10)
# - Generate a random number as a string of N digits
#   -> Ensure no leading zeros

# 2. Game Loop
# - Repeat until user guesses correctly OR out of guesses:
#     - Get input from user
#     - Validate input (length, digits only, etc.)
#     - Compare with target number
#     - Provide clues:
#         - "Fermi"  → correct digit, correct position
#         - "Pico"   → correct digit, wrong position
#         - "Bagels" → no correct digits
#     - Decrease remaining chances

# 3. Post Game
# - If guessed correctly: Congratulate the user
# - If out of chances: Show the correct number
# - Ask if the user wants to play again

# 4. Replay Logic
# - If yes: restart with fresh number and reset chances
# - If no: exit the game with a goodbye message

import random


def generate_number(MAX_DIGITS):
    """generates a random MAX_DIGITS long number using random module"""
    return  str(random.randint(10 ** (MAX_DIGITS-1), 10 ** MAX_DIGITS - 1))

def compare(user_number, computer_number):
    """Compares the number with computer generated and return a string and boolean, if won then true else false"""
    if user_number == computer_number:
        return "You have got it correct!", True
    else:
        output = []
        for i in range(len(computer_number)):
            if computer_number[i] == user_number[i]:
                output.append("Fermi")
            elif user_number[i] in computer_number:
                output.append("Pico")
        else:
            if len(output) == 0:
                output.append("Bagels")
        random.shuffle(output)
        return " ".join(output), False

def game_start(MAXIMUM_CHANCES,MAX_DIGITS):
    """this has the core logic of the game - includes game loop and life line loop"""
    print("Welcome to the Bagels Game!")
    print("Try to guess the number. Clues:")
    print("- Fermi: correct digit in correct position")
    print("- Pico: correct digit in wrong position")
    print("- Bagels: no correct digits\n")
    running = True
    while running: #GAME-LOOP
       chances = MAXIMUM_CHANCES
       print(f"Computer is thinking of a number of {MAX_DIGITS} digits long.")
       computer_number = generate_number(MAX_DIGITS)
       is_won = False
       while chances > 0: #LIFE_LINE LOOP
           user_number = input("Please enter your number: ")
           output, is_won = compare(user_number,computer_number)
           print(output)
           if is_won:
               break
           else:
               chances -= 1
               print(f"You have {chances} more chances left, Try again.")

       if not is_won:
           print("Sorry, you lost!")
       print(f"The computer number was {computer_number}")
       play_again = input("Do you want to play again? (y/n): ")
       if play_again == "n":
           print("Thank you for playing!")
           running = False
       else:
           continue

def main():
    MAX_DIGITS = 3
    MAXIMUM_CHANCES = 10
    game_start(MAXIMUM_CHANCES,MAX_DIGITS)

if __name__ == "__main__":
    main()