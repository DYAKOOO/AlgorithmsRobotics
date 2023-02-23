
## Problem Statement:

# There is a robot starting at position (0, 0), the origin, on a 2D plane. 
#Given a sequence of its moves, moves, consisting of uppercase English letters 'L', 'R', 'U', and 'D', 
#representing left, right, up, and down respectively, return true if the robot returns to the origin 
#after it finishes all of its moves, or false otherwise.

# The robot's moves are as follows:

#     It takes exactly one step in the direction specified by moves[i].
#     The robot never revisits a position it has previously visited.

# Note that the initial direction of the robot facing north is not specified explicitly in the input, but can be inferred from the sequence of moves.

# Example:

# Input: moves = "UD"

# Output: true

# Explanation: The robot moves up once, and then down once. All moves have the same magnitude, 
#so it ended up at the origin where it started. Therefore, we return true.

# Constraints:

#     1 <= moves.length <= 2 * 10^4
#     moves only contains the characters 'U', 'D', 'L' and 'R'.


##############
#First Alternative 
###############
#Import the Libraries
# from typing import List

# # Initialize the variables. 
# position = [0, 0]
# origin = [0, 0]
# moves = ['L', 'R', 'U', 'D']

# # The function takes in moves and the origin and returns a boolean of true and false. 
# def RobotReturn(moves: List[str], origin: List[int]) -> bool:
#     for move in moves:
#         if move == 'L':
#             position[0] -= 1
#         elif move == 'R':
#             position[0] += 1 
#         elif move == 'D':
#             position[1] -= 1
#         elif move == 'U':
#             position[1] +=1 
#     if position == origin:
#         return True
#     else:
#         return False
###################
#Second Alternative
###################

from typing import List

def isRobotReturn(moves: List[str], origin: List[int]) -> bool:
    # Initialize the variables.
    position = [0, 0]
    move_map = {'L': [-1, 0], 'R': [1, 0], 'U': [0, 1], 'D': [0, -1]}
    
    # Execute the moves and update the position.
    for move in moves:
        position[0] += move_map[move][0]
        position[1] += move_map[move][1]
    
    # Check if the final position is the same as the origin.
    return position == origin




        
    
    

        
            
        







