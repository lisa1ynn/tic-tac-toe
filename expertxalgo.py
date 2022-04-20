# importing random, as the algorithm should keep the player on their toes, not playing in the same corner every time, for instance
import random

# defining lists for corners, sides and the center. This will ease the process of selecting random corners, for example
allspaces=[1,2,3,4,5,6,7,8,9]
alreadyusedspaces=[]
originalcorners=[1,3,7,9]
corners=[1,3,7,9]
sides=[2,4,6,8]
center=5


# move 1

# if computer is x, take a corner, using the random.choice method, choosing a random corner
firstX=""
def Expertmove1x():
    global firstX
    firstX=random.choice(corners)
    return firstX

# A function between moves to delete an already used part of the list from the list
def listremover(number):
    global corners
    global sides
    if number in corners:
        corners.remove(number)
    elif number in sides:
        sides.remove(number)




Expertmove1x()
print(corners)
print(firstX)
listremover(firstX)
print(corners)
# move 2

# X: if o put it in the center, place x in the corner opposite to 1st x
# if o put it in any corner, put x in any corner
# if o put in on a side, put x in center

def Expertmove2x(firstX,firstO):
    global secondX
    if firstX in originalcorners and firstO==center:
        if firstX==1:
            secondX = 9
        elif firstX==3:
            secondX = 7
        elif firstX==7:
            secondX = 3
        else:
            secondX = 1
    elif firstX in originalcorners and firstO in originalcorners:
        secondX = random.choice(corners)
    else:
        secondX = center
    return secondX

Expertmove2x(firstX,random.choice(corners))
print(secondX)


# we need a function to make a 3 in a row if possible
# to do that, we need a list of sets of 2 in a rows, with a possible 3rd, eg. {1,5}, with a possible 9 being 3 in a row
# note that {2,6} are two in a diagonal row, but there cannot be 3 in a row like that

possible3inrows=[{1,2},{1,3},{2,3},{4,5},{4,6},{5,6},{7,9},{8,9},{7,8},{1,4},{1,7},{4,7},{2,5},{2,8},{5,8},{3,6},{3,9},{6,9},{1,5},{1,9},{5,9},{3,5},{3,7},{5,7}]

# now we need sets of actual 3 in a rows

actual3inrows=[{1,2,3},{4,5,6},{7,8,9},{1,4,7},{2,5,8},{3,6,9},{1,5,9},{3,5,7}]


def winthegameX():
    if {firstX,secondX} in possible3inrows:
        for element in allspaces:
            if {firstX,secondX,element} in actual3inrows:
                return element



# move 3

# X: connect 3, if possible

winthegameX()

# if not, block O from connecting 3

# we need a similar function to see if O can win the game
firstO=""
secondO=""

def winthegameO():
    if {firstO,secondO} in possible3inrows:
        for element in allspaces:
            if {firstO,secondO,element} in actual3inrows:
                return element



winthegameO()

# threaten two connect 3s simultaneously
# while designing the function, it occured to me that a list of already used spaces could be useful.
# After each move, a function should append the move to the list
# we also need a function that will check if a certain 3 in a row is already blocked by an O
# we also need a sort of lookup function, where by passing 2 items of a potential 3 in a row set will return the entire set

def threeinrow(firstone,secondone):
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

def isnotblocked(firstone,secondone):
    if threeinrow(firstone,secondone)-{firstone,secondone} in allspaces:
        return True

def threatentowinX():
    for element in allspaces:
        if {firstX,element} in possible3inrows and {secondX,element} in possible3inrows:
            if isnotblocked({firstX,element}) and isnotblocked({secondX,element}):
                return element




# any other space, if the other functions do not return a value
def anyothermove():
    return random.choice(allspaces)


# now we have to put all the functions in order for the final function and tell them to proceed until a value is returned


def Expertmove3x(firstX,firstO,secondX,secondO):
    winthegameX()
    if winthegameX() not in allspaces:
        winthegameO()
    elif (winthegameO() and winthegameX()) not in allspaces:
        threatentowinX()
    elif (winthegameO()and winthegameX() and threatentowinX()) not in allspaces:
        anyothermove()



# move 4

#X: connect 3 if possible
# elif block O from connecting 3
# random place

# we need a modified win the game function, as 2 more moves have been played since it was last used
thirdX=""
def winthegameX2():
    if {firstX,secondX} in possible3inrows:
        for element in allspaces:
            if {firstX,secondX,element} in actual3inrows:
                return element
    elif {firstX,thirdX} in possible3inrows:
        for element in allspaces:
            if {firstX,thirdX,element} in actual3inrows:
                return element
    elif {thirdX,secondX} in possible3inrows:
        for element in allspaces:
            if {thirdX,secondX,element} in actual3inrows:
                return element


# now we need to modify the previous function to block O from making 3 in a row
thirdO=""

def winthegameO2():
    if {firstO,secondO} in possible3inrows:
        for element in allspaces:
            if {firstO,secondO,element} in actual3inrows:
                return element
    elif {firstO,thirdO} in possible3inrows:
        for element in allspaces:
            if {firstO,thirdO,element} in actual3inrows:
                return element
    elif {secondO, thirdO} in possible3inrows:
        for element in allspaces:
            if {secondO, thirdO, element} in actual3inrows:
                return element

def Expertmove4x(firstX,firstO,secondX,secondO,thirdX,thirdO):
    winthegameX2()
    if winthegameX2() not in allspaces:
        winthegameO2()
    elif (winthegameO2() and winthegameX2()) not in allspaces:
        anyothermove()


# move 5

#X: the last space

def Expertmove5x():
    anyothermove()










