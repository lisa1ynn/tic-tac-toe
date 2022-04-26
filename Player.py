class Player:
    def __init__(self, symbol, name):
        self.__name = name
        self.__symbol = symbol
        self.__moves = []
        self.__time = " "
        self.__highscore = " "

    #Returns player name
    def getName(self):
        return self.__name

    #changes player name
    def setName(self):
        name = input(f"{self.__name}, what is your name?: ")
        self.__name = name

    #asks the player to make a move and returns it
    def makeMove(self):
        try:
            move = int(input(f"{self.__name}, is your next move? (1-9): "))
            return move
        except ValueError:
            return

    #returns the symbol
    def getSymbol(self):
        return self.__symbol

    #returns high score of player
    def getHighscore(self):
        return

    #asks the players if they want to swith signs after starting a new game
    def switchSigns(self):
        return

    #saves the move of the player to their dashboard
    def saveMove(self):
        return


