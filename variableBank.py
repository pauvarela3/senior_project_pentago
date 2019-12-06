from pprint import pprint

# failed attempt to refactor if statements in 'drop_piece' function
# out of range errors


# 3D array
variablenum = [
    # board representation of all variables in rotation 0
    [
     [0, 1, 2, 3, 4, 5],
     [6, 7, 8, 9, 10, 11],
     [12, 13, 14, 15, 16, 17],
     [18, 19, 20, 21, 22, 23],
     [24, 25, 26, 27, 28, 29],
     [30, 31, 32, 33, 34, 35]
    ],

    # board representation of all variables in rotation 1
    [
     [12, 6, 0, 15, 9, 3],
     [13, 7, 1, 16, 10, 4],
     [14, 8, 2, 17, 11, 5],
     [30, 24, 18, 33, 27, 21],
     [31, 25, 19, 34, 28, 22],
     [32, 26, 20, 35, 29, 23]
    ],

    # board representation of all variables in rotation 2
    [
     [14, 13, 12, 17, 16, 15],
     [8, 7, 6, 11, 10, 9],
     [2, 1, 0, 5, 4, 3],
     [32, 31, 30, 35, 34, 33],
     [26, 25, 24, 29, 28, 27],
     [20, 19, 18, 23, 22, 21]
    ],

    # board representation of all variables in rotation 3
    [
     [2, 8, 14, 5, 11, 17],
     [1, 7, 13, 4, 10, 16],
     [0, 6, 12, 3, 9, 15],
     [20, 26, 32, 23, 29, 35],
     [19, 25, 31, 22, 28, 34],
     [18, 24, 30, 21, 27, 33]
    ]
]

# if you know the rotation of the quad, just search board row and column

# testing
# test = variablenum[0][5][2]
# print("test should be 32")
# print(test)
#
# test2= variablenum[0][2][5]
# print("test2 should be 17")
# print(test2)


def findVariable(rot, r, c):
    return variablenum[rot][c-1][r-1]
    # subtracting row and column by 1 because
    # rows/cols in array reprseented by 0-5
    # rows/cols in pentagoClass represented by 1-6

# //



# # pentagoClass code
#
# def drop_piece(self, row, col):
#     global quad_0_rotation
#     global quad_1_rotation
#     global quad_2_rotation
#     global quad_3_rotation
#
#     # beginning of refactoring
#
#     # find correct quad
#     if row < 4 and col < 4
#         quad = 0
#
#     if row < 4 and col > 3
#         quad = 1
#
#     if row > 3 and col < 4
#         quad = 2
#
#     if row > 3 and quad > 3
#         quad = 3
#
#     # finding correct quad rotation
#     rotation = globals()['quad_' + str(quad) + '_rotation']
#
#     # find variable via lookup
#     variable_number = variableBank.findVariable(rotation, row, col)
#
#
#     # end of refactoring
#
#     # rest of code...
#     AI.score_taking(variable_number, self.turn)
#
#     AI_Defense.score_taking(variable_number, self.turn)
#     if self.turn == 0:
#         piece = 1
#     else:
#         piece = 2
#
#     if not self.valid_move(row, col, quad):
#         return self.turn
#     else:
#         self.board[quad][row][col] = piece
#         self.top += 1
#         self.moves[self.top][0] = self.turn + 1
#         self.moves[self.top][1] = quad
#         self.moves[self.top][2] = row
#         self.moves[self.top][3] = col
#
#         if self.winning_move(1):
#             self.player1 = True
#         if self.winning_move(2):
#             self.player2 = True
#         if self.player1 and self.player2:
#             self.draw = True
#             self.state = 3
#         elif self.player1 or self.player2:
#             self.state = 2
