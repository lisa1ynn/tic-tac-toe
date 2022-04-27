from Player import Player
from Game import Game
from datetime import datetime

# main function that brings everything together
def main():

    #as long as otherGame varibale is True, the game will continue and the player will be asked whom to play with
    otherGame = True
    while otherGame == True:

        #asks user which mode they want to play and saves it in a variable
        mode = input("Whom do you want to play against? (other player = 1, easy computer = 2, expert computer = 3): ")

        #is started if a player wants to play against another player
        if mode == "1":

            #creates a new game object
            game = Game()

            #greets players and creates them
            playerX = Player(symbol="X", name="Player X")
            playerX.setName()
            print(f"Hello {playerX.getName()}, you will play first.")

            playerO = Player(symbol="O", name="Player O")
            playerO.setName()
            print(f"Hello {playerO.getName()}, you will play second.")

            #saves start time and date of players
            startDateTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            game.addPlayTime(playerX, playerO, startDateTime)

            # as long as otherPlayerGame variable is True,
            # the game with the same player will continue
            otherPlayerGame = True
            while otherPlayerGame == True:

                #starts game
                game.playAgainstPlayer(playerX, playerO)

                # changes signs and turns of players so
                # the player who started last time comes second now
                playerX, playerO = playerO, playerX
                playerX.changeSymbol()
                playerO.changeSymbol()

                #Asks player if they want to play another round with this player or not
                #Repreats game if they said "yes", and ends it if they said "no"
                playAgain = input("Do you want to play another round together? (yes/ no): ")
                if playAgain != "yes":
                    otherPlayerGame = False


        else:
            #placeholder for easy and hard computer
            print("This mode is not available right now.")

        #as long as otherGame varibale is True, the game will repeat
        #if they answer no, print "Game over! and end game"
        repeatGame = input("Do you want to play again with another player? (yes/ no): ")
        if repeatGame != "yes":
            otherGame = False
            print("Game over!")


main()
