#  The program allows the user to input one of four directions, the user then travels to that direction
#  depending on wether the direction is valid. Once the user has reached the end tile a message is displayed.
#  The user starts on a tile [1, 1] and the victory tile is [3, 1]. 
#  This should be able to be accomplished with ifelse loops inside a function and a while loop running in the main program.

def validDirection(position, direction):
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
            return False

    elif position == "1,3":
        if direction == "e":
            return "2,3"
        elif direction == "s":
            return "1,2"
        else:
            return False
    
    elif position == "2,1":
        if direction == "n":
            return "2,2"
        else:
            return False

    elif position == "2,2":
        if direction == "w":
            return "1,2"
        elif direction == "s":
            return "2,1"
        else:
            return False
    
    elif position == "2,3":
        if direction == "e":
            return "3,3"
        elif direction == "w":
            return "1,3"
        else:
            return False
    
    elif position == "3,2":
        if direction == "n":
            return "3,3"
        elif direction == "s":
            return "3,1"
        else:
            return False

    elif position == "3,3":
        if direction == "w":
            return "2,3"
        elif direction == "s":
            return "3,2"
        else:
            return False

def validDirections(position):
    if position == "1,1":
        return "(N)orth"
    elif position == "1,2":
        return "(N)orth or (E)ast or (S)outh"

#Variables
currentTile = "1,1"
victoryTile = "3,1"
nextTile = ""
notValidMsg = False

# senda direction alltaf med .lower()
while currentTile != victoryTile:
    print("You can travel:", str(validDirections(currentTile))+".")
    
    nextTile = input("Direction: ")

    if validDirection(currentTile, nextTile):
        currentTile = validDirection(currentTile, nextTile)
        print(currentTile)
        print(notValidMsg)
    else:
        print("Not a valid direction!")

    


else:
    print("Victory!")