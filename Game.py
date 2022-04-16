class Game:
    def __init__(self, number):
        self.__number = number
        self.__duration = " "
        self.__timestamps = " "

    #returns number of game
    def getNumber(self):
        return