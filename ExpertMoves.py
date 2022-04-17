# move 1

# if computer is x, take a corner, probably some randint from 1 to 4
# if computer is o, take the center, if open. If x takes center, take a corner

# move 2

# X: if o put it in the center, place x in the corner opposite to 1st x
# if o put it in any corner, put x in any corner
# if o put in on a side, put x in center

# O: block X if needed
# if there are two X on opposite corner with o  in middle, put it on a side
# if 1xcorner,1omiddle, 2x side, where not threatening to win, put o in corner between the 2 x
# if 1st o between 2 xs, put o anywhere
# if 2xs on adjacent sides, put o in either corner, where it touches x
# if x1 center, x2 corner, put o in corner


# move 3

# X: connect 3, if possible
# if not, block O from connecting 3
# threaten two connect 3s simultaneously
# any other space

#O: connect 3, if possible
# elif block X from connecting 3
# threaten 2 connect 3s simultaneously
# any other space

# move 4

#X: connect 3 if possible
# elif block O from connecting 3
# random place

#O: connect 3
# block X from connect 3
# any other space

# move 5

#X: the last space

