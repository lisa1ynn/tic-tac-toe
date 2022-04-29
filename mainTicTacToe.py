from Player import Player
from Game import Game
from datetime import datetime
from ComputerBeginner import BeginnerGame
from ComputerExpert import ExpertGame

# main function that brings everything together
def main():

    # as long as otherGame varibale is True, the game will continue and the player will be asked whom to play with
    otherGame = True
    while otherGame == True:

        # asks user which mode they want to play and saves it in a variable
        mode = input("Whom do you want to play against? (other player = 1, easy computer = 2, expert computer = 3): ")

        # is started if a player wants to play against another player
        if mode == "1":

            # creates a new game object
            game = Game()

            # greets players, creates them, and updates their names to the players' names
            playerX = Player(symbol="X", name="Player X")
            playerX.setName()
            print(f"Hello {playerX.getName()}, you will play first.")

            playerO = Player(symbol="O", name="Player O")
            playerO.setName()
            print(f"Hello {playerO.getName()}, you will play second.")

            # saves start time and date of players
            startDateTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            game.addPlayTime(playerX, playerO, startDateTime)

            # as long as otherPlayerGame variable is True,
            # the game with the same player will continue
            otherPlayerGame = True
            while otherPlayerGame == True:

                # starts game
                game.playAgainstPlayer(playerX, playerO)

                # changes symbols and turns of players so
                # the player who started last time comes second now
                playerX, playerO = playerO, playerX
                playerX.changeSymbol()
                playerO.changeSymbol()

                # asks player if they want to play another round with this player or not
                # repeats game if they said "yes", and ends it if they said "no"
                playAgain = input("Do you want to play another round together? (yes/ no): ")
                if playAgain != "yes":
                    otherPlayerGame = False

        # started when player wants to play against a beginner computer
        elif mode == "2":

            # creates a new BeginnerGame object
            beginnergame=BeginnerGame()

            # greets the player, creates them, and updates their name to the player's name
            playerX = Player(symbol="X", name="Player X")
            playerX.setName()
            print(f"Hello {playerX.getName()}, you will play first.")
            computer = Player(symbol="O", name="Computer Simulated Beginner")

            # saves start time and date of players
            startDateTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            beginnergame.addPlayTime(playerX, computer, startDateTime)

            # set a counter to alternate X and O
            counter = 2
            # as long as otherPlayerGame variable is True,
            # the game with the same player will continue
            otherPlayerGame = True
            while otherPlayerGame == True:


                # set and increment a counter, so that the game alternates between player playing as X and as O


                if counter%2==0:
                    # starts game
                    beginnergame.playAgainstBeginnerX(playerX, computer)
                else:
                    beginnergame.playAgainstBeginnerO(playerX, computer)



                # increment the counter
                counter+=1

                # asks player if they want to play another round with this player or not
                # repeats game if they said "yes", and ends it if they said "no"
                playAgain = input("Do you want to play another round together? (yes/ no): ")
                if playAgain != "yes":
                    otherPlayerGame = False


        # started when player wants to play against a beginner computer
        elif mode == "3":

            # creates a new BeginnerGame object
            expertgame = ExpertGame()

            # greets the player, creates them, and updates their name to the player's name
            playerX = Player(symbol="X", name="Player X")
            playerX.setName()
            print(f"Hello {playerX.getName()}, you will play first.")
            computer = Player(symbol="O", name="Computer Simulated Beginner")

            # saves start time and date of players
            startDateTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            expertgame.addPlayTime(playerX, computer, startDateTime)

            # set a counter to alternate X and O
            counter = 2
            # as long as otherPlayerGame variable is True,
            # the game with the same player will continue
            otherPlayerGame = True
            while otherPlayerGame == True:

                # set and increment a counter, so that the game alternates between player playing as X and as O

                if counter % 2 == 0:
                    # starts game
                    expertgame.playAgainstExpertX(playerX, computer)
                else:
                    expertgame.playAgainstExpertO(playerX, computer)

                # increment the counter
                counter += 1

                # asks player if they want to play another round with this player or not
                # repeats game if they said "yes", and ends it if they said "no"
                playAgain = input("Do you want to play another round together? (yes/ no): ")
                if playAgain != "yes":
                    otherPlayerGame = False


        # as long as otherGame varibale is True, the game will repeat
        # if they answer no, print "Game over! and end game"
        repeatGame = input("Do you want to play again with another player? (yes/ no): ")
        if repeatGame != "yes":
            otherGame = False
            print("Game over!")


main()
