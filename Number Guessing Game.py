import random
import os ,time

def game():


    print ("""welcom to the Number Guessing Game !
I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.""")
    
    choice =   int(input("\nPlease select the difficulty level:\n" \
    "1. Easy (10 chance)\n" \
    "2. Medium (5 chance)\n" \
    "3. Hard (3 chance)\n" \
    "" \
    "\nEnter your choice : "))

    try :
        if choice == 1 :
            print (f"\nGreat! You have selected the Easy difficulty level.\nLet's start the game!")
            chance = 10
        elif choice == 2 :
            print (f"\nGreat! You have selected the Medium difficulty level.\nLet's start the game!")
            chance = 5
        elif choice == 3 :
            print (f"\nGreat! You have selected the Hard difficulty level.\nLet's start the game!")
            chance = 3
        else :
            
            os.system("cls")
            print ("\nPlease Enter the number between 1 , 3 \n")
            time.sleep(4)
            game()
    except ValueError :
        
        os.system("cls")
        print ("Please enter a number between 1 ,3  ")
        time.sleep(4)
        game()
    
    start_game (chance)



def start_game(all_chance):

    chance = all_chance
    r_num = random.randint(1,100)

    while chance != 0:
        try :
            guess = int(input("Enter your guess : "))

            if guess != r_num :
                if guess > r_num :
                    print (f"Incorrect! The number is less than {guess}")
                else :
                    print (f"Incorrect! The number is greater than {guess}")
                chance -=1
            else :
                print (f"Congratulations! You guessed the correct number in {all_chance-chance} attempts.")
                break

        except ValueError:

            print ("Please enter correct number !! ")

    else :
        print ("Sorry , You used all chance you have !")
        print (f"The number is {r_num}")

        

game()
