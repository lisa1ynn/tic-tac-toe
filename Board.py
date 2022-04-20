

class Board:
    def __init__(self):
        self.__spaces = ["1","2","3","4","5","6","7","8","9"]


    #prints playing board in console 
    def getBoard(self):
        print("-------------------\n"
                f"|  {self.__spaces[0]}  |  {self.__spaces[1]}  |  {self.__spaces[2]}  |\n"
                "-------------------\n"
                f"|  {self.__spaces[3]}  |  {self.__spaces[4]}  |  {self.__spaces[5]}  |\n"
                "-------------------\n"
                f"|  {self.__spaces[6]}  |  {self.__spaces[7]}  |  {self.__spaces[8]}  |\n"
                "-------------------")

    #Checks if move is valid
    def isValidMove(self, move):
        if move in range(1,10) and str(move) in self.__spaces:
            return True

    #Updates board after move has been done and checked
    def updateBoard(self, symbol, move):
        self.__spaces[move - 1] = symbol

    #Checks if one of the winner cases took place
    def isWinner(self):
        for i in [0, 3, 6]:
            if self.__spaces[i] == self.__spaces[i + 1] == self.__spaces[i + 2]:
                return True

        for i in [0, 1, 2]:
            if self.__spaces[i] == self.__spaces[i + 3] == self.__spaces[i + 6]:
                return True

        if self.__spaces[0] == self.__spaces[4] == self.__spaces[8] or self.__spaces[2] == self.__spaces[4] == self.__spaces[6]:
            return True

    #Checks if the game is a draw
    def isDraw(self):
        for i in self.__spaces:
            if i in ["1","2","3","4","5","6","7","8","9"]:
                return False

    #Asks the players if they want to play again
    def setRestart(self):
        return






