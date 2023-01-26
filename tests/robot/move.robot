*** Setting ***
Documentation  I want to move my character. If they attempt to move past a boundary, the move resutls in no change in position.
Test Template  Move character
Library  MoveLibrary.py

*** Test Cases ***     StartingX  StartingY  StartingCount    Direction   EndingX  EndingY EndingCount
Move in middle of board  0           0           10            NORTH       0       1         11  
Move on edge of board    0           0            5            SOUTH       0       0          6
From 1,6 move North      1           6            7            NORTH       1       7          8
From 1,6 move South      1           5           12            SOUTH       1       5         13
From 1,6 move East       2           6           54            EAST        2       6         55 
From 1,6 move West       1           6          103            WEST        0       6        104
From 0,0 move South      0           0            3            SOUTH       0       0          4    
From 0,0 move West       0           0            7            WEST        0       0          8  
From 9,9 move North      9           9           23            NORTH       9       9         24
From 9,9 move East       9           9           43            EAST        9       9         44



*** Keywords ***
Move character
    [Arguments]   ${startingX}  ${startingY}  ${startingCount}  ${direction}  ${endingX}  ${endingY}  ${endingCount}
    Initialize character xposition with     ${startingX}
    Initialize character yposition with     ${startingY}
    Initialize character moveCount with     ${startingCount}
    Move in direction                       ${direction}
    Character xposition should be           ${endingX}
    Character yposition should be           ${endingY}
    Character movecount should be           ${endingCount} 