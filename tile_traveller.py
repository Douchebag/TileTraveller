#  The program allows the user to input one of four directions, the user then travels to that direction
#  depending on wether the direction is valid. Once the user has reached the end tile a message is displayed.
#  The user starts on a tile [1, 1] and the victory tile is [3, 1]. 
#  This should be able to be accomplished with ifelse loops inside a function and a while loop running in the main program.

def validDirection(position, direction):
    notValidMsg = "Not a valid direction!"
    if position == "1,1":
        if direction == "n":
            return "1,2"
        else:
            return False
    elif position == "1,2":
        if direction == "n":
            return "1,3"
        elif direction == "s":
            return "1,1"
        elif direction == "e":
            return "2,2"
        else:
            return notValidMsg

def validDirections(position):
    if position == "1,1":
        return "(N)orth"
    elif position == "1,2":
        return "(N)orth or (E)ast or (S)outh"

#Variables
currentTile = "1,1"
victoryTile = "3,1"
nextTile = ""

# senda direction alltaf med .lower()
while currentTile != victoryTile:
    print("You can travel:", validDirections(currentTile) + ".")

    nextTile = input("Direction: ")

    validDirection(currentTile, nextTile)
    currentTile == nextTile

    


else:
    print("Victory!")