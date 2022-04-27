from Board import Board
from vegetable import veggies
import time
import random


# creates Game class, initiates an object of class, and assigns states
class Game:
    def __init__(self):
        self.__startTime = " "
        self.__duration = " "


    # starts a game against another player
    def playAgainstPlayer(self, playerX, playerO):

        # Initialize new board object and assign each player a position (current or next)
        board = Board()
        currentPlayer, nextPlayer = playerX, playerO

        # saves beginning time of game
        self.__startTime = time.time()

        # executes a new move as long as there is no winner or draw case
        while board.isWinner() != True and board.isDraw() != True:
            board.getBoard()
            move = currentPlayer.makeMove()

            # checks if move is valid. As long as it is not valid, ask for another move.
            while board.isValidMove(move) != True:
                move = currentPlayer.makeMove()

            # update board by exchanging the number with the player sign and switch turns
            board.updateBoard(currentPlayer.getSymbol(), move)
            nextPlayer, currentPlayer = currentPlayer, nextPlayer

        # if the game ends through a win or draw, the board is printed once more and the winner/ draw message is printed
        # if there is a winner, add new high score of player to their name in file
        board.getBoard()
        if board.isWinner():
            print(f"Congratulations, {nextPlayer.getName()}, you won!")
            print(f"{currentPlayer.getName()}, you little {veggies[random.randint(0, 56)]}! YOU LOST!!!")

            # updates high score of winner
            self.updateHighScore(nextPlayer)

        else:
            # if game is a draw
            print(f"{currentPlayer.getName()}, you little {veggies[random.randint(0, 56)]}, "
                  f"{nextPlayer.getName()}, you little {veggies[random.randint(0, 56)]}, "
                  f"NO ONE WON...this is a DRAW!!!")

        # calculates duration of game and prints it
        self.__duration = time.time() - self.__startTime
        print(f"This game had a duration of {round(self.__duration/60)} minute(s) "
              f"and {round(self.__duration%60)} second(s).")


    #updates high score in player script file
    def updateHighScore(self, nextPlayer):
        # open or create playerFile with names high scores, and play times
        playerFile = open("Player_script.txt")

        # create list from all lines and close playerFile
        playerList = playerFile.readlines()
        playerFile.close()

        # increases high score number of winner by one if name is already in file
        if f"Player: {nextPlayer.getName()}\n" in playerList:

            # finds index of list item with winner name and gets high score index
            # through adding 1
            highScoreIndex = int(playerList.index(f"Player: {nextPlayer.getName()}\n")) + 1

            # adds one to current high score and adds new string back top list
            highScore = str(int(playerList[highScoreIndex][12:-1]) + 1)
            playerList[highScoreIndex] = f"High score: {highScore}\n"

        # opens Player_script.txt file with write mode and joins the playerList to one string
        playerFile = open("Player_script.txt", "w")
        playerFileContent = "".join(playerList)

        # writes updated content inside file and closes it
        playerFile.write(playerFileContent)
        playerFile.close()

        # prints high score of winner
        print(f"{nextPlayer.getName()}, your high score is {highScore}")


    # adds time and date played to players in players script file
    def addPlayTime(self, nextPlayer, currentPlayer, startDateTime):
        # open or create playerFile with names high scores, and play times
        playerFile = open("Player_script.txt")

        # create list from all lines and close playerFile
        playerList = playerFile.readlines()
        playerFile.close()

        # adds play time of players if names are already in file
        for player in [currentPlayer, nextPlayer]:
            if f"Player: {player.getName()}\n" in playerList:

                # finds index of list item with player name and adds time played
                timePlayedIndex = int(playerList.index(f"Player: {player.getName()}\n")) + 3

                #adds start date and time of current game to Player_script.txt file
                playerList.insert(timePlayedIndex, f"    {startDateTime}\n")

            else:
                # adds name of new player with high score of 0 and time played to file
                playerList.append(f"Player: {player.getName()}\n")
                playerList.append("High score: 0\n")
                playerList.append("Times played: \n")
                playerList.append(f"    {startDateTime}\n")
                playerList.append("\n")

            # opens Player_script.txt file with write mode and joins the playerList to one string
            playerFile = open("Player_script.txt", "w")
            playerFileContent = "".join(playerList)

            # writes updated content inside file and closes it
            playerFile.write(playerFileContent)
            playerFile.close()
