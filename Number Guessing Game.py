import random  # Library to generate random numbers
import os ,time  # os for system commands (like clearing the screen), time for delays

# --------------------------------------
# Main function to start the game
# Asks the player to choose difficulty level
# and sets the number of attempts
# --------------------------------------

def game():


    print ("""welcom to the Number Guessing Game !
I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.""")

    # Player chooses difficulty level: Easy (10 attempts), Medium (5 attempts), Hard (3 attempts)
    choice =   int(input("\nPlease select the difficulty level:\n" \
    "1. Easy (10 chance)\n" \
    "2. Medium (5 chance)\n" \
    "3. Hard (3 chance)\n" \
    "" \
    "\nEnter your choice : "))

    try :
        if choice == 1 :
            print (f"\nGreat! You have selected the Easy difficulty level.\nLet's start the game!")
            chance = 10  # Number of attempts for Easy
            
        elif choice == 2 :
            print (f"\nGreat! You have selected the Medium difficulty level.\nLet's start the game!")
            chance = 5  # Number of attempts for Medium
            
        elif choice == 3 :
            print (f"\nGreat! You have selected the Hard difficulty level.\nLet's start the game!")
            chance = 3   # Number of attempts for Hard
            
        else :
             # If input is not 1, 2, or 3 → restart the game
 
            os.system("cls")# Clear the screen (works on Windows)
            
            print ("\nPlease Enter the number between 1 , 3 \n")
            time.sleep(4)
            game()
            
    except ValueError :
         # If the user enters a non-integer value
        
        os.system("cls")
        print ("Please enter a number between 1 ,3  ")
        time.sleep(4)
        game()

    # Start the actual guessing game
    start_game (chance)


# --------------------------------------
# Function to run the guessing game
# Parameters:
#   all_chance → total attempts based on difficulty
# Generates a random number and lets the player guess
# --------------------------------------

def start_game(all_chance):

    chance = all_chance    # Store the number of remaining attempts
    r_num = random.randint(1,100)   # Random number between 1 and 100

    # Loop until the player runs out of chances or guesses correctly
    while chance != 0:
        try :
            guess = int(input("Enter your guess : ")) # Player's guess

            if guess != r_num :
                
                # Wrong guess → give a hint (higher/lower)
                if guess > r_num :
                    print (f"Incorrect! The number is less than {guess}")
                else :
                    print (f"Incorrect! The number is greater than {guess}")
                chance -=1   # Decrease number of attempts
                
            else :
                 # Correct guess
                print (f"Congratulations! You guessed the correct number in {all_chance-chance} attempts.")
                break

        except ValueError:
            
             # Handle invalid input
            print ("Please enter correct number !! ")

    else :
        
         # If no attempts left
        print ("Sorry , You used all chance you have !")
        print (f"The number is {r_num}")

        
# Call the main function to start the game
game()

