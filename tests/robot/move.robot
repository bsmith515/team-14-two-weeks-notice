*** Setting ***
Documentation  I want to move my character. If they attempt to move past a boundary, the move resutls in no change in position.
Test Template  Move character
Library  MoveLibrary.py

*** Test Cases ***     StartingX  StartingY  Direction   EndingX  EndingY 
Move in middle of board  0           0          NORTH       0       1     
Move on edge of board    0           0          SOUTH       0       0     
From 1,6 move North      1           6          NORTH       1       7     
From 1,6 move South      1           5          SOUTH       1       5     
From 1,6 move East       2           6          EAST        2       6     
From 1,6 move West       1           6          WEST        0       6     
From 0,0 move South      0           0          SOUTH       0       0     
From 0,0 move West       0           0          WEST        0       0     
From 9,9 move North      9           9          NORTH       9       9     
From 9,9 move East       9           9          EAST        9       9    



*** Keywords ***
Move character
    [Arguments]   ${startingX}  ${startingY}  ${direction}  ${endingX}  ${endingY}
    Initialize character xposition with     ${startingX}
    Initialize character yposition with     ${startingY}
    Move in direction                       ${direction}
    Character xposition should be           ${endingX}
    Character yposition should be           ${endingY}