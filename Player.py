# creates Player class, initiates an object of class, and assigns states
class Player:
    def __init__(self, symbol, name):
        self.__name = name
        self.__symbol = symbol


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
            move = int(input(f"{self.__name}, what is your next move? (1-9): "))
            return move
        except ValueError:
            return


    #returns the symbol
    def getSymbol(self):
        return self.__symbol


    #changes the symbol
    def changeSymbol(self):
        if self.__symbol == "X":
            self.__symbol = "O"
        else:
            self.__symbol = "X"
