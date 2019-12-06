
# node variables contained in respective quadrants
quad_0_variables = [0, 1, 2, 6, 7, 8, 12, 13, 14]
quad_1_variables = [3, 4, 5, 9, 10, 11, 15, 16, 17]
quad_2_variables = [18, 19, 20, 24, 25, 26, 30, 31, 32]
quad_3_variables = [21, 22, 23, 27, 28, 29, 33, 34, 35]

# node variables for quads mapped to vector representing rotations
# first element in vector == row and column of rotation 0,
# 2nd element == rotation 1, 3rd element == rotation 2, 4th element == rotation 3
quad_0_hash = {0: [[1, 1], [1, 3], [3, 3], [3, 1]],
               1: [ [1,2], [2,3], [3,2], [2,1] ],
               2: [ [1,3], [3,3], [3,1], [1,1] ],
               6: [ [2,1], [1,2], [2,3], [3,2] ],
               7: [ [2,2], [2,2], [2,2], [2,2] ],
               8: [ [2,3], [3,2], [2,1], [1,2] ],
               12: [ [3,1], [1,1], [1,3], [3,3] ],
               13: [ [3,2], [2,1], [1,2], [2,3] ],
               14: [ [3,3], [3,1], [1,1], [1,3] ]
               }

quad_1_hash = {3: [[1, 4], [1, 6], [3, 6], [3, 4]],
               4: [ [1,5], [2,6], [3,5], [2,4] ],
               5: [ [1,6], [3,6], [3,4], [1,4] ],
               9: [ [2,4], [1,5], [2,6], [3,5] ],
               10: [ [2,5], [2,5], [2,5], [2,5] ],
               11: [ [2,6], [3,5], [2,4], [1,5] ],
               15: [ [3,4], [1,4], [1,6], [3,6] ],
               16: [ [3,5], [2,4], [1,5], [2,6] ],
               17: [ [3,6], [3,4], [1,4], [1,6] ]
               }

quad_2_hash = {18: [[4, 1], [4, 3], [6, 3], [6, 1]],
               19: [ [4,2], [5,3], [6,2], [5,1] ],
               20: [ [4,3], [6,3], [6,1], [4,1] ],
               24: [ [5,1], [4,2], [5,3], [6,2] ],
               25: [ [5,2], [5,2], [5,2], [5,2] ],
               26: [ [5,3], [6,2], [5,1], [4,2] ],
               30: [ [6,1], [4,1], [4,3], [6,3] ],
               31: [ [6,2], [5,1], [4,2], [5,3] ],
               32: [ [6,3], [6,1], [4,1], [4,3] ]
               }

quad_3_hash = {21: [[4, 4], [4, 6], [6, 6], [6, 4]],
               22: [ [4,5], [5,6], [6,5], [5,4] ],
               23: [ [4,6], [6,6], [6,4], [4,4] ],
               27: [ [5,4], [4,5], [5,6], [6,5] ],
               28: [ [5,5], [5,5], [5,5], [5,5] ],
               29: [ [5,6], [6,5], [5,4], [4,5] ],
               33: [ [6,4], [4,4], [4,6], [6,6] ],
               34: [ [6,5], [5,4], [4,5], [5,6] ],
               35: [ [6,6], [6,4], [4,4], [4,6] ]
               }

# hash representing complete board
# 0 = quad 0, 1 = quad 1, etc
board_hash = {0: quad_0_hash, 1: quad_1_hash, 2: quad_2_hash, 3: quad_3_hash}

# access row ==> board_hash[quad][node_variable][rotation][0]
# access col ==> board_hash[quad][node_variable][rotation][1]



# testing below

# node_variable = 6
# print(f'test variable: {node_variable}')

# rotation = 3
# print(f'rotation: {rotation}')

# if (node_variable in quad_0_variables):
#     quad = 0
# if (node_variable in quad_1_variables):
#     quad = 1
# if (node_variable in quad_2_variables):
#     quad = 2
# if (node_variable in quad_3_variables):
#     quad = 3

# print(f'quad: {quad}')

# row = board_hash[quad][node_variable][rotation][0]
# column = board_hash[quad][node_variable][rotation][1]
# print(f'row: {row}')
# print(f'column: {column}')

# rotation = globals()[('quad_')+str(quad)+('_rotation')]
# print(f'rotation: {rotation}')