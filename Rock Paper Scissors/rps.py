import random 


options = ["rock", "paper", "scissors"]

winConditions = {"paper" : "rock", "rock" : "scissors", "scissors" : "paper"}


def game():

    ## Variable Declaration ##
    current_round = 1
    player_wins = 0
    computer_wins = 0
    player_choice = ""
    cpu_choice = ""

    out_of = 0

    ## BEST OUT OF X ROUNDS ERROR CHECKING AND INPUT FROM USER
    while True:

        try:
            out_of = int(input("\nBest out of ___ ?\n>> "))
            break
        except:
            print("\nInvalid input. Try again.")
            continue

    
    ## RUNS TILL CONDITIONS ARE MET, WHEN CONDITIONS ARE MET THEY BREAK FROM THE LOOP ##
    while (True):

            if player_wins == ((out_of // 2) + 1):
                print("You won!")
                break
            elif computer_wins == ((out_of // 2) + 1):
                print("The computer won!")
                break


             ### GAME STATS ###
             
            print("\n\nCurrent round: " + str(current_round))
            print("Player wins: " + str(player_wins))
            print("Computer wins: " + str(computer_wins))
               
            ### USER INPUT ###  
            print("\n[Rock] [Paper] [Scissors]")
            player_choice = input("\n>> ")
            cpu_choice = random.choice(options)
           

            ### User Input Error Checking ###
            while(player_choice.casefold().strip() not in options):

                    print("\nInvalid Input. Try Again.\n")
                    print("[Rock] [Paper] [Scissors]")
                    player_choice = input(">> ")

            ### WHAT WAS PLAYED ###
            print("\n\n\n\n\n\n\n\n--------------------------------")
            print("\nPlayer played " + player_choice)
            print("Computer played " + cpu_choice + "\n")
            
            
           ## Checks if Player Input beats Computer Input
            if(player_choice in winConditions.keys()):
                if (cpu_choice == winConditions[player_choice]):
                        print("\nYou won round " + str(current_round) + "!")
                        print("--------------------------------\n\n\n")
                        player_wins += 1 # Adds a win for the player

            ## Checks if Computer Input beats Player Input
            if(cpu_choice in winConditions.keys()):
                if (player_choice == winConditions[cpu_choice]):
                    print("\nComputer won round " + str(current_round) + "!")
                    print("--------------------------------\n\n\n")
                    computer_wins += 1 # Adds a win for the computer

            ## If both inputs are equal to each other
            if(cpu_choice == player_choice):
                print("Its a draw!\n")
                print("--------------------------------\n\n\n")
            
            current_round += 1

    ## Asks if user wants to play again
    again = input("\n\nWould you like to go again? [1] for yes, [2] for no\n>> ")
    while again.strip() not in ["1","2"]:
        print("\n\nInvalid input. Try again. \n")
        again = input("Would you like to go again? [1] for yes, [2] for no\n>> ")

    # Recursion if player wants to play again
    if (again.strip() == "1"):
        game()
    else:
        pass

game()






