from Board import Board
from vegetable import veggies
import time
import random
from Algorithm import Algo



class ExpertGame:
    def __init__(self):
        self.__startTime = " "
        self.__duration = " "

# starts a game against the beginner computer as player with X
    def playAgainstExpertX(self, playerX, computer):

        # Initialize new board object
        board = Board()
        currentPlayer, nextPlayer = playerX, computer

        # saves beginning time of game
        self.__startTime = time.time()

        # initializes the algorithm
        algo = Algo()

        # executes the first move

        board.getBoard()
        firstX = playerX.makeMove()

        # checks if move is valid. As long as it is not valid, ask for another move.
        while board.isValidMove(firstX) != True:
            firstX = playerX.makeMove()

        # update board by exchanging the number with the player sign
        board.updateBoard("X", firstX)

        # the first move is removed from the available moves for the algorithm
        algo.listremover(firstX)
        algo.listremoverall(firstX)


        # the algorithm makes the first move
        firstO = algo.Expertmove1O()
        algo.setfirstO(firstO)
        # update board by exchanging the number with the player sign
        board.updateBoard("O", firstO)

        # the first move is removed from the available moves for the algorithm
        algo.listremover(firstO)
        algo.listremoverall(firstO)

        # the process for X making moves repeats, while the process for the computer making moves is similar, only different functions are used
        board.getBoard()
        secondX = playerX.makeMove()

        # checks if move is valid. As long as it is not valid, ask for another move.
        while board.isValidMove(secondX) != True:
            secondX = playerX.makeMove()

        # update board by exchanging the number with the player sign
        board.updateBoard("X", secondX)

        # the second move is removed from the available moves for the algorithm
        algo.listremover(secondX)
        algo.listremoverall(secondX)

        # the algorithm makes the second move
        # the first and second X variables are set
        algo.setfirstX(firstX)
        algo.setsecondX(secondX)

        secondO = algo.Expertmove2O()
        algo.setsecondO(secondO)
        # update board by exchanging the number with the player sign
        board.updateBoard("O", secondO)

        # the first move is removed from the available moves for the algorithm
        algo.listremover(secondO)
        algo.listremoverall(secondO)


        # third X
        board.getBoard()
        thirdX = playerX.makeMove()


        # checks if move is valid. As long as it is not valid, ask for another move.
        while board.isValidMove(thirdX) != True:
            thirdX = playerX.makeMove()
        algo.setthirdX(thirdX)
        # update board by exchanging the number with the player sign
        board.updateBoard("X", thirdX)

        # the second move is removed from the available moves for the algorithm
        algo.listremover(thirdX)
        algo.listremoverall(thirdX)

        # executes a new move as long as there is no winner or draw case
        if board.isWinner() != True and board.isDraw() != True:

            # the algorithm makes the third move
            thirdO = algo.Expertmove3O()
            algo.setthirdO(thirdO)
            # update board by exchanging the number with the player sign
            board.updateBoard("O", thirdO)

            # the first move is removed from the available moves for the algorithm
            algo.listremover(thirdO)
            algo.listremoverall(thirdO)

            # switches the player and the computer for the purposes of printing the correct names in the right order at the end of the game
            nextPlayer, currentPlayer = currentPlayer, nextPlayer

            # executes a new move as long as there is no winner or draw case
            if board.isWinner() != True and board.isDraw() != True:

                # fourth X
                board.getBoard()
                fourthX = playerX.makeMove()

                # checks if move is valid. As long as it is not valid, ask for another move.
                while board.isValidMove(fourthX) != True:
                    fourthX = playerX.makeMove()
                algo.setfourthX(fourthX)
                # update board by exchanging the number with the player sign
                board.updateBoard("X", fourthX)

                # the second move is removed from the available moves for the algorithm
                algo.listremover(fourthX)
                algo.listremoverall(fourthX)

                # switches the player and the computer for the purposes of printing the correct names in the right order at the end of the game
                nextPlayer, currentPlayer = currentPlayer, nextPlayer

                # executes a new move as long as there is no winner or draw case
                if board.isWinner() != True and board.isDraw() != True:

                    # the algorithm makes the fourth move
                    fourthO = algo.Expertmove4O()

                    # update board by exchanging the number with the player sign
                    board.updateBoard("O", fourthO)

                    # the first move is removed from the available moves for the algorithm
                    algo.listremover(fourthO)
                    algo.listremoverall(fourthO)

                    # switches the player and the computer for the purposes of printing the correct names in the right order at the end of the game
                    nextPlayer, currentPlayer = currentPlayer, nextPlayer

                    # executes a new move as long as there is no winner or draw case
                    if board.isWinner() != True and board.isDraw() != True:

                        # last X
                        board.getBoard()
                        lastX = playerX.makeMove()

                        # checks if move is valid. As long as it is not valid, ask for another move.
                        while board.isValidMove(lastX) != True:
                            lastX = playerX.makeMove()

                        # update board by exchanging the number with the player sign
                        board.updateBoard("X", lastX)

                        # switches the player and the computer for the purposes of printing the correct names in the right order at the end of the game
                        nextPlayer, currentPlayer = currentPlayer, nextPlayer

                # if the game ends through a win or draw, the board is printed once more and the winner/ draw message is printed
                # High score is not added in the file, as only multiplayer games should count
            board.getBoard()
            if board.isWinner():
                print(f"Congratulations, {currentPlayer.getName()}, you won!")
                print(f"{nextPlayer.getName()}, you little {veggies[random.randint(0, 55)]}! YOU LOST!!!")



            else:
                # if game is a draw
                print(
                    f"HAHAHA, YOU CAN'T BEAT ME, {playerX.getName().upper()}, YOU LITTLE {veggies[random.randint(0, 55)].upper()}!!!")

            # calculates duration of game and prints it
            self.__duration = time.time() - self.__startTime
            print(f"This game had a duration of {round(self.__duration / 60)} minute(s) "
                  f"and {round(self.__duration % 60)} second(s).")

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

                    # adds start date and time of current game to Player_script.txt file
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


    def playAgainstExpertO(self,playerX, computer):

        # Initialize new board object
        board = Board()
        currentPlayer, nextPlayer = computer, playerX

        # saves beginning time of game
        self.__startTime = time.time()

        # initializes the algorithm
        algo = Algo()

        # executes the first move


        firstX = algo.Expertmove1x()
        # set firstX
        algo.setfirstX(firstX)

        # update board by exchanging the number with the player sign
        board.updateBoard("X", firstX)

        # the first move is removed from the available moves for the algorithm
        algo.listremover(firstX)
        algo.listremoverall(firstX)

        board.getBoard()
        # the player makes the first move
        firstO = playerX.makeMove()
        algo.setfirstO(firstO)
        # update board by exchanging the number with the player sign
        board.updateBoard("O", firstO)

        # the first move is removed from the available moves for the algorithm
        algo.listremover(firstO)
        algo.listremoverall(firstO)

        # the process for X making moves repeats, while the process for the computer making moves is similar, only different functions are used
        board.getBoard()
        secondX = algo.Expertmove2x()

        # update board by exchanging the number with the player sign
        board.updateBoard("X", secondX)

        # the second move is removed from the available moves for the algorithm
        algo.listremover(secondX)
        algo.listremoverall(secondX)

        # the algorithm makes the second move
        # the second X variable is set
        algo.setsecondX(secondX)

        board.getBoard()

        secondO = playerX.makeMove()
        # checks if move is valid. As long as it is not valid, ask for another move.
        while board.isValidMove(secondO) != True:
            secondO = playerX.makeMove()
        algo.setsecondO(secondO)
        # update board by exchanging the number with the player sign
        board.updateBoard("O", secondO)

        # the first move is removed from the available moves for the algorithm
        algo.listremover(secondO)
        algo.listremoverall(secondO)

        # third X
        thirdX = algo.Expertmove3x()


        algo.setthirdX(thirdX)
        # update board by exchanging the number with the player sign
        board.updateBoard("X", thirdX)

        # the second move is removed from the available moves for the algorithm
        algo.listremover(thirdX)
        algo.listremoverall(thirdX)

        # executes a new move as long as there is no winner or draw case
        if board.isWinner() != True and board.isDraw() != True:

            board.getBoard()
            # the algorithm makes the third move
            thirdO = playerX.makeMove()
            while board.isValidMove(thirdO) != True:
                thirdO = playerX.makeMove()
            algo.setthirdO(thirdO)
            # update board by exchanging the number with the player sign
            board.updateBoard("O", thirdO)

            # the first move is removed from the available moves for the algorithm
            algo.listremover(thirdO)
            algo.listremoverall(thirdO)

            # switches the player and the computer for the purposes of printing the correct names in the right order at the end of the game
            nextPlayer, currentPlayer = currentPlayer, nextPlayer

            # executes a new move as long as there is no winner or draw case
            if board.isWinner() != True and board.isDraw() != True:

                # fourth X

                fourthX = algo.Expertmove4x()

                # checks if move is valid. As long as it is not valid, ask for another move.
                algo.setfourthX(fourthX)
                # update board by exchanging the number with the player sign
                board.updateBoard("X", fourthX)

                # the second move is removed from the available moves for the algorithm
                algo.listremover(fourthX)
                algo.listremoverall(fourthX)

                # switches the player and the computer for the purposes of printing the correct names in the right order at the end of the game
                nextPlayer, currentPlayer = currentPlayer, nextPlayer

                # executes a new move as long as there is no winner or draw case
                if board.isWinner() != True and board.isDraw() != True:
                    board.getBoard()
                    # the algorithm makes the fourth move
                    fourthO = playerX.makeMove()

                    while board.isValidMove(fourthO) != True:
                        fourthO = playerX.makeMove()
                    # update board by exchanging the number with the player sign
                    board.updateBoard("O", fourthO)

                    # the first move is removed from the available moves for the algorithm
                    algo.listremover(fourthO)
                    algo.listremoverall(fourthO)

                    # switches the player and the computer for the purposes of printing the correct names in the right order at the end of the game
                    nextPlayer, currentPlayer = currentPlayer, nextPlayer

                    # executes a new move as long as there is no winner or draw case
                    if board.isWinner() != True and board.isDraw() != True:

                        # last X

                        lastX = algo.Expertmove5x()

                        # update board by exchanging the number with the player sign
                        board.updateBoard("X", lastX)

                        # switches the player and the computer for the purposes of printing the correct names in the right order at the end of the game
                        nextPlayer, currentPlayer = currentPlayer, nextPlayer

                # if the game ends through a win or draw, the board is printed once more and the winner/ draw message is printed
                # High score is not added in the file, as only multiplayer games should count
            board.getBoard()
            if board.isWinner():
                print(f"Congratulations, {currentPlayer.getName()}, you won!")
                print(f"{nextPlayer.getName()}, you little {veggies[random.randint(0, 55)]}! YOU LOST!!!")



            else:
                # if game is a draw
                print(f"HAHAHA, YOU CAN'T BEAT ME, {playerX.getName().upper()}, YOU LITTLE {veggies[random.randint(0, 55)].upper()}!!!")

            # calculates duration of game and prints it
            self.__duration = time.time() - self.__startTime
            print(f"This game had a duration of {round(self.__duration / 60)} minute(s) "
                  f"and {round(self.__duration % 60)} second(s).")

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

                # adds start date and time of current game to Player_script.txt file
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
