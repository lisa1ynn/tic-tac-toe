# X Move 1:
# Places the X into a random square, as a beginner does not possess the foresight to predict opponents moves

# importing random, as the algorithm should keep the player on their toes, not playing in the same corner every time, for instance
import random

class Algo:

    def __init__(self):
    # defining lists for corners, sides and the center. This will ease the process of selecting random corners, for example
        self.__allspaces=[1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.__alreadyusedspaces=[]
        self.__originalcorners=[1,3,7,9]
        self.__corners=[1,3,7,9]
        self.__sides=[2,4,6,8]
        self.__center=5
        self.__possible3inrows=[{1,2},{1,3},{2,3},{4,5},{4,6},{5,6},{7,9},{8,9},{7,8},{1,4},{1,7},{4,7},{2,5},{2,8},{5,8},{3,6},{3,9},{6,9},{1,5},{1,9},{5,9},{3,5},{3,7},{5,7}]
        self.__actual3inrows = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}]
        self.__oppositecorners = [{1, 9}, {3, 7}]
        self.__cornersidesituation = [{1, 6}, {1, 8}, {3, 4}, {3, 8}, {7, 2}, {7, 6}, {9, 2}, {9, 4}]
        self.__oppositesides = [{2, 8}, {4, 6}]
        self.__adjacentsides = [{2, 4}, {2, 6}, {4, 8}, {6, 8}]
        self.__firstX = 10
        self.__secondX = 10
        self.__thirdX = 10
        self.__fourthX = 10
        self.__firstO = 10
        self.__secondO = 10
        self.__thirdO = 10



    # defining functions to change variables

    def setfirstX(self,firstX):
        self.__firstX = firstX

    def setsecondX(self,secondX):
        self.__secondX = secondX

    def setthirdX(self,thirdX):
        self.__thirdX = thirdX

    def setfourthX(self,fourthX):
        self.__fourthX = fourthX

    def setfirstO(self,firstO):
        self.__firstO = firstO

    def setsecondO(self,secondO):
        self.__secondO = secondO

    def setthirdO(self,thirdO):
        self.__thirdO = thirdO




    # expert move 1

    # if computer is x, take a corner, using the random.choice method, choosing a random corner
    def Expertmove1x(self):
        return random.choice(self.__corners)


    # A function between moves to delete an already used part of the list from the list
    def listremover(self,number):
        if number in self.__corners:
            self.__corners.remove(number)
        elif number in self.__sides:
            self.__sides.remove(number)

    # A function between moves to delete an already used part of the allspaces list from the list
    def listremoverall(self,number):
        self.__allspaces.remove(number)



    # move 2

    # X: if o put it in the center, place x in the corner opposite to 1st x
    # if o put it in any corner, put x in any corner
    # if o put in on a side, put x in center

    def Expertmove2x(self):
        if self.__firstX in self.__originalcorners and self.__firstO==self.__center:
            if self.__firstX==1:
                return 9
            elif self.__firstX==3:
                return 7
            elif self.__firstX==7:
                return 3
            else:
                return 1
        elif self.__firstX in self.__originalcorners and self.__firstO in self.__originalcorners:
            return random.choice(self.__corners)
        else:
            return self.__center





    # we need a function to make a 3 in a row if possible
    # to do that, we need a list of sets of 2 in a rows, with a possible 3rd, eg. {1,5}, with a possible 9 being 3 in a row
    # note that {2,6} are two in a diagonal row, but there cannot be 3 in a row like that

    possible3inrows=[{1,2},{1,3},{2,3},{4,5},{4,6},{5,6},{7,9},{8,9},{7,8},{1,4},{1,7},{4,7},{2,5},{2,8},{5,8},{3,6},{3,9},{6,9},{1,5},{1,9},{5,9},{3,5},{3,7},{5,7}]

    # now we need sets of actual 3 in a rows

    actual3inrows=[{1,2,3},{4,5,6},{7,8,9},{1,4,7},{2,5,8},{3,6,9},{1,5,9},{3,5,7}]


    def winthegameX(self):
        if {self.__firstX,self.__secondX} in self.__possible3inrows:
            for element in self.__allspaces:
                if {self.__firstX,self.__secondX,element} in self.__actual3inrows:
                    return element



    # move 3

    # X: connect 3, if possible



    # if not, block O from connecting 3

    # we need a similar function to see if O can win the game


    def winthegameO(self):
        if {self.__firstO,self.__secondO} in self.__possible3inrows:
            for element in self.__allspaces:
                if {self.__firstO,self.__secondO,element} in self.__actual3inrows:
                    return element





    # threaten two connect 3s simultaneously
    # while designing the function, it occured to me that a list of already used spaces could be useful.
    # After each move, a function should append the move to the list
    # we also need a function that will check if a certain 3 in a row is already blocked by an O
    # we also need a sort of lookup function, where by passing 2 items of a potential 3 in a row set will return the entire set

    def threeinrow(self,firstone,secondone):
        if {firstone,secondone}=={1,2} or {firstone,secondone}=={3,2} or{firstone,secondone}=={1,3}:
            return {1,2,3}
        elif {firstone,secondone}=={4,5} or {firstone,secondone}=={4,6} or{firstone,secondone}=={5,6}:
            return {4,5,6}
        elif {firstone,secondone}=={7,8} or {firstone,secondone}=={7,9} or{firstone,secondone}=={8,9}:
            return {7,8,9}
        elif {firstone,secondone}=={1,4} or {firstone,secondone}=={4,7} or{firstone,secondone}=={1,7}:
            return {1,4,7}
        elif {firstone,secondone}=={2,5} or {firstone,secondone}=={2,8} or{firstone,secondone}=={5,8}:
            return {2,5,8}
        elif {firstone,secondone}=={3,6} or {firstone,secondone}=={9,6} or{firstone,secondone}=={3,9}:
            return {3,6,9}
        elif {firstone,secondone}=={1,5} or {firstone,secondone}=={1,9} or{firstone,secondone}=={5,9}:
            return {1,5,9}
        elif {firstone,secondone}=={3,5} or {firstone,secondone}=={3,7} or{firstone,secondone}=={5,7}:
            return {3,5,7}

    def isnotblocked(self, firstone,secondone):
        for i in (self.threeinrow(firstone,secondone)-{firstone,secondone}):
            if i in self.__allspaces:
                return True


    def threatentowinX(self):
        for element in self.__allspaces:
            if {self.__firstX,element} in self.__possible3inrows and {self.__secondX,element} in self.__possible3inrows:
                if self.isnotblocked(self.__firstX,element) and self.isnotblocked(self.__secondX,element):
                    return element




    # any other space, if the other functions do not return a value
    def anyothermove(self):
        return random.choice(self.__allspaces)


    # now we have to put all the functions in order for the final function and tell them to proceed until a value is returned


    def Expertmove3x(self):
        if self.winthegameX() in self.__allspaces:
            return self.winthegameX()
        elif self.winthegameX() not in self.__allspaces and self.winthegameO() in self.__allspaces:
            return self.winthegameO()
        elif (self.winthegameO() and self.winthegameX()) not in self.__allspaces and self.threatentowinX() in self.__allspaces:
            return self.threatentowinX()
        else:
            return self.anyothermove()



    # move 4

    #X: connect 3 if possible
    # elif block O from connecting 3
    # random place

    # we need a modified win the game function, as 2 more moves have been played since it was last used

    def winthegameX2(self):
        if {self.__firstX,self.__secondX} in self.__possible3inrows:
            for element in self.__allspaces:
                if {self.__firstX,self.__secondX,element} in self.__actual3inrows:
                    return element
        if {self.__firstX,self.__thirdX} in self.__possible3inrows:
            for space in self.__allspaces:
                if {self.__firstX,self.__thirdX,space} in self.__actual3inrows:
                    return space
        if {self.__thirdX,self.__secondX} in self.__possible3inrows:
            for move in self.__allspaces:
                if {self.__thirdX,self.__secondX,move} in self.__actual3inrows:
                    return move



    # now we need to modify the previous function to block O from making 3 in a row
    thirdO=""

    def winthegameO2(self):
        if {self.__firstO,self.__secondO} in self.__possible3inrows:
            for element in self.__allspaces:
                if {self.__firstO,self.__secondO,element} in self.__actual3inrows:
                    return element
        if {self.__firstO,self.__thirdO} in self.__possible3inrows:
            for element in self.__allspaces:
                if {self.__firstO,self.__thirdO,element} in self.__actual3inrows:
                    return element
        if {self.__secondO, self.__thirdO} in self.__possible3inrows:
            for element in self.__allspaces:
                if {self.__secondO, self.__thirdO, element} in self.__actual3inrows:
                    return element

    def Expertmove4x(self):
        if self.winthegameX2() in self.__allspaces:
            return self.winthegameX2()
        elif self.winthegameX2() not in self.__allspaces and self.winthegameO2() in self.__allspaces:
            return self.winthegameO2()
        else:
            return self.anyothermove()


    # move 5

    #X: the last space

    def Expertmove5x(self):
        return self.anyothermove()





    # move 1

    # if computer is o, take the center, if open. If x takes center, take a corner

    def Expertmove1O(self):
        if self.__firstX == self.__center:
            return random.choice(self.__corners)
        else:
            return self.__center


    # move 2

    # O: block X if needed


    # if there are two X on opposite corner with o  in middle, put it on a side

    # lets define a list of sets of opposite corners

    oppositecorners= [{1,9},{3,7}]

    def sidetrickO(self):
        if self.__firstO==self.__center and ({self.__firstX,self.__secondX} in self.__oppositecorners):
            return random.choice(self.__sides)


    # if 1xcorner,1omiddle, 2x side, where not threatening to win, put o in corner between the 2 x

    # we need to define sets where X are in a corner and a side, but not threatening to win

    cornersidesituation=[{1,6},{1,8},{3,4},{3,8},{7,2},{7,6},{9,2},{9,4}]

    def cornertrickO(self):
        if self.__firstO==self.__center and ({self.__firstX,self.__secondX} in self.__cornersidesituation):
            if {self.__firstX,self.__secondX}=={1,6}:
                return 3
            elif {self.__firstX,self.__secondX}=={1,8}:
                return 7
            elif {self.__firstX,self.__secondX}=={3,4}:
                return 1
            elif {self.__firstX,self.__secondX}=={3,8}:
                return 9
            elif {self.__firstX,self.__secondX}=={7,2}:
                return 1
            elif {self.__firstX,self.__secondX}=={7,6}:
                return 9
            elif {self.__firstX,self.__secondX}=={9,2}:
                return 3
            elif {self.__firstX,self.__secondX}=={9,4}:
                return 7

    # if 1st o between 2 xs on sides, put o anywhere

    # similarly, we need a list of sets where 2 Xs are on opposite sides

    oppositesides=[{2,8},{4,6}]

    def funnyline(self):
        if self.__firstO==self.__center and ({self.__firstX,self.__secondX} in self.__oppositesides):
            return random.choice(self.__allspaces)

    # if 2xs on adjacent sides, put o in either corner, where it touches x

    # again, we need a new list of 2xs on adjacent sides

    adjacentsides=[{2,4},{2,6},{4,8},{6,8}]

    def boringsideline(self):
        if self.__firstO==self.__center and ({self.__firstX,self.__secondX} in self.__adjacentsides):
            if {self.__firstX, self.__secondX} == {2, 6}:
                return random.choice([1,3,9])
            elif {self.__firstX, self.__secondX} == {2, 4}:
                return random.choice([1,3,7])
            elif {self.__firstX, self.__secondX} == {8, 6}:
                return random.choice([7,3,9])
            elif {self.__firstX, self.__secondX} == {4, 8}:
                return random.choice([1,7,9])

    # if x1 center, x2 corner, put o in corner

    def centerXresponse(self):
        if self.__firstX==self.__center and self.__secondX in self.__originalcorners:
            return random.choice(self.__corners)


    def Expertmove2O(self):
        if self.winthegameX() in self.__allspaces:
            return self.winthegameX()
        elif self.winthegameX() not in self.__allspaces and self.sidetrickO() in self.__allspaces:
            return self.sidetrickO()
        elif (self.winthegameX() and self.sidetrickO()) not in self.__allspaces and self.cornertrickO() in self.__allspaces:
            return self.cornertrickO()
        elif (self.winthegameX() and self.sidetrickO() and self.cornertrickO()) not in self.__allspaces and self.funnyline() in self.__allspaces:
            return self.funnyline()
        elif (self.winthegameX() and self.sidetrickO() and self.cornertrickO() and
              self.funnyline()) not in self.__allspaces and self.boringsideline() in self.__allspaces:
            return self.boringsideline()
        else:
            return self.centerXresponse()



    # move 3


    #O: connect 3, if possible
    # we already have this function


    # elif block X from connecting 3
    # we already have this function

    # threaten 2 connect 3s simultaneously
    # we need to slightly modify the function for X, but we essentially have this one already

    def threatentowinO(self):
        for element in self.__allspaces:
            if {self.__firstO,element} in self.__possible3inrows and {self.__secondO,element} in self.__possible3inrows:
                if self.isnotblocked({self.__firstO,element}) and self.isnotblocked({self.__secondO,element}):
                    return element

    # any other space





    def Expertmove3O(self):
        if self.winthegameO() in self.__allspaces:
            return self.winthegameO()
        elif self.winthegameO() not in self.__allspaces and self.winthegameX2() in self.__allspaces:
            return self.winthegameX2()
        elif (self.winthegameX2() and self.winthegameO()) not in self.__allspaces and self.threatentowinO() in self.__allspaces:
            return self.threatentowinO()
        else:
            return self.anyothermove()



    # move 4

    #O: connect 3
    # we already have this function

    # block X from connect 3

    # we also already have this function
    # But we need a modified win the game function, as 4  moves have been played for X

    def winthegameX3(self):
        if {self.__firstX,self.__secondX} in self.__possible3inrows:
            for element in self.__allspaces:
                if {self.__firstX,self.__secondX,element} in self.__actual3inrows:
                    return element
        if {self.__firstX,self.__thirdX} in self.__possible3inrows:
            for element in self.__allspaces:
                if {self.__firstX,self.__thirdX,element} in self.__actual3inrows:
                    return element
        if {self.__thirdX,self.__secondX} in self.__possible3inrows:
            for element in self.__allspaces:
                if {self.__thirdX,self.__secondX,element} in self.__actual3inrows:
                    return element
        if {self.__firstX,self.__fourthX} in self.__possible3inrows:
            for element in self.__allspaces:
                if {self.__firstX,self.__fourthX,element} in self.__actual3inrows:
                    return element
        if {self.__thirdX,self.__fourthX} in self.__possible3inrows:
            for element in self.__allspaces:
                if {self.__thirdX,self.__fourthX,element} in self.__actual3inrows:
                    return element
        if {self.__secondX, self.__fourthX} in self.__possible3inrows:
            for element in self.__allspaces:
                 if {self.__secondX, self.__fourthX, element} in self.__actual3inrows:
                    return element


    # any other space

    def Expertmove4O(self):
        if self.winthegameO2() in self.__allspaces:
            return self.winthegameO2()
        elif self.winthegameO2() not in self.__allspaces and self.winthegameX3() in self.__allspaces:
            return self.winthegameX3()
        else:
            return self.anyothermove()



    # Beginner Moves

    # Rationale: The beginner does not see moves ahead, cannot predict what their opponent will play. But they know how to win.
    # This also means that they know how to prevent their oponnent from winning, if possible.
    # If they cannot prevent the opponent from winning or win themselves they put the move in a random space




    def Beginnermove1x(self):
        return self.anyothermove()

    def Beginnermove2x(self):
        return self.anyothermove()

    def Beginnermove3x(self):
        if self.winthegameX() in self.__allspaces:
            return self.winthegameX()
        if self.winthegameX() not in self.__allspaces and self.winthegameO() in self.__allspaces:
            return self.winthegameO()
        else:
            return self.anyothermove()

    def Beginnermove4x(self):
        if self.winthegameX2() in self.__allspaces:
            return self.winthegameX2()
        if self.winthegameX2() not in self.__allspaces and self.winthegameO2() in self.__allspaces:
            return self.winthegameO2()
        else:
            return self.anyothermove()

    def Beginnermove5x(self):
        return self.anyothermove()


    # Now the moves for O, the rationale is the same

    def Beginnermove1O(self):
        return self.anyothermove()



    def Beginnermove2O(self):
        if self.winthegameX() in self.__allspaces:
            return self.winthegameX()
        if self.winthegameX() not in self.__allspaces:
            return self.anyothermove()


    def Beginnermove3O(self):
        first = self.winthegameO()
        second = self.winthegameX2()
        if first in self.__allspaces:
            return first
        elif first not in self.__allspaces and second in self.__allspaces:
            return second
        else:
            return self.anyothermove()



    def Beginnermove4O(self):
        if self.winthegameO2() in self.__allspaces:
            return self.winthegameO2()
        if self.winthegameO2() not in self.__allspaces and self.winthegameX3() in self.__allspaces:
            return self.winthegameX3()
        else:
            return self.anyothermove()






