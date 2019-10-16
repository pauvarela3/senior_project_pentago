import numpy as np
import pygame
import sys
import math
BLUE = (0,0,255)
DARKBLUE = (0,0,139)
BLACK = (0,0,0)
WHITE = (255,255,255)
ROW_COUNT = 3
COLUMN_COUNT = 3
SQUARE_COUNT = 4
SQUARESIZE = 100
RADIUS = int(SQUARESIZE/2 - 5)
Red_Circle = pygame.image.load("Red_Circle.jpg")
def create_board():
        board = np.zeros((4,ROW_COUNT,COLUMN_COUNT))
        return board
#put piece
def drop_piece(board, square, row, col, piece):
    board[square][row][col] = piece
#check if you can put a
def is_valid_location(board, square, col, row):
    return board[square][row][col] == 0
#drop the ficha
def get_next_open_row(board, square, col):
    for r in range(ROW_COUNT):
        if board[square][r][col] == 0:
            return r
def rotate_a_square_counter_clockwise(board,square):
        board[square] = np.rot90(board[square],1)
def rotate_a_square_clockwise(board,square):
        board[square] = np.rot90(board[square],3)
        
        print("look")
        print(board)
        print("look")
def print_board(board):
    print(np.flip(board, 0))
board = create_board()
print(board)
game_over = False
turn = 0
def winning_move(board,piece):
    #check for horizontal wins
    """for c in range(COLUMN_COUNT-4):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece and board[r][c+4] == piece:
                return True

    #check for vertical wins
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-4):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece and board[r+4][c] == piece:
                return True
    #check positively slope
    for c in range(COLUMN_COUNT-4):
        for r in range(ROW_COUNT-4):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece and board[r+4][c+4] == piece:
                return True
    #check negatively slope
    for c in range(COLUMN_COUNT-4):
        for r in range(2,ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece and board[r-4][c+4] == piece:
                return True        """
def draw_board(board):
        for s in range (SQUARE_COUNT):
            for c in range (COLUMN_COUNT):
                for r in range (ROW_COUNT):
                        if s == 0:
                                pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
                                pygame.draw.circle(screen, DARKBLUE, (int(c*SQUARESIZE + SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)),RADIUS)
                        elif s == 1:
                                pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, (math.ceil(ROW_COUNT/2)+1 + r)*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
                                pygame.draw.circle(screen, DARKBLUE, (int(c*SQUARESIZE + SQUARESIZE/2), int((math.ceil(ROW_COUNT/2)+1+r)*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)),RADIUS)
                        elif s == 2:
                                pygame.draw.rect(screen, BLUE, ((math.ceil(COLUMN_COUNT/2)+1+c)*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
                                pygame.draw.circle(screen, DARKBLUE, (int((math.ceil(COLUMN_COUNT/2)+1+c)*SQUARESIZE + SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)),RADIUS)
                        elif s == 3:
                                pygame.draw.rect(screen, BLUE, ((math.ceil(COLUMN_COUNT/2)+1+c)*SQUARESIZE, (math.ceil(ROW_COUNT/2)+1+r)*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
                                pygame.draw.circle(screen, DARKBLUE, (int((math.ceil(COLUMN_COUNT/2)+1+c)*SQUARESIZE + SQUARESIZE/2), int((math.ceil(ROW_COUNT/2)+1+r)*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)),RADIUS)

        for s in range (SQUARE_COUNT):
            for c in range (COLUMN_COUNT):
                for r in range (ROW_COUNT):
                        if s == 0: 
                            if board[s][r][c] == 1:
                                pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE + SQUARESIZE/2), int((1+r)*SQUARESIZE+SQUARESIZE/2)),RADIUS)
                            elif board[s][r][c] == 2:
                                pygame.draw.circle(screen, WHITE, (int(c*SQUARESIZE + SQUARESIZE/2), int((1+r)*SQUARESIZE+SQUARESIZE/2)),RADIUS)
                        elif s == 1:
                            if board[s][r][c] == 1:   
                                pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE + SQUARESIZE/2), int((math.ceil(ROW_COUNT/2)+2 + r)*SQUARESIZE+SQUARESIZE/2)),RADIUS)
                            elif board[s][r][c] == 2:
                                pygame.draw.circle(screen, WHITE, (int(c*SQUARESIZE + SQUARESIZE/2), int((math.ceil(ROW_COUNT/2)+2 + r)*SQUARESIZE+SQUARESIZE/2)),RADIUS)
                        elif s == 2:
                            if board[s][r][c] == 1:   
                                pygame.draw.circle(screen, BLACK, (int((math.ceil(COLUMN_COUNT/2)+1+c)*SQUARESIZE + SQUARESIZE/2), int((r+1)*SQUARESIZE+SQUARESIZE/2)),RADIUS)
                            elif board[s][r][c] == 2:
                                pygame.draw.circle(screen, WHITE, (int((math.ceil(COLUMN_COUNT/2)+1+c)*SQUARESIZE + SQUARESIZE/2), int((r+1)*SQUARESIZE+SQUARESIZE/2)),RADIUS)
                        elif s == 3:
                            if board[s][r][c] == 1:   
                                pygame.draw.circle(screen, BLACK, (int((math.ceil(COLUMN_COUNT/2)+1+c)*SQUARESIZE + SQUARESIZE/2), int((math.ceil(ROW_COUNT/2)+2 + r)*SQUARESIZE+SQUARESIZE/2)),RADIUS)
                            elif board[s][r][c] == 2:
                                pygame.draw.circle(screen, WHITE, (int((math.ceil(COLUMN_COUNT/2)+1+c)*SQUARESIZE + SQUARESIZE/2), int((math.ceil(ROW_COUNT/2)+2 + r)*SQUARESIZE+SQUARESIZE/2)),RADIUS)

        pygame.display.update()
pygame.init()
state = 0
width = COLUMN_COUNT * SQUARESIZE * 2
height = (ROW_COUNT)* SQUARESIZE * 2 + SQUARESIZE

size = (width,height)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen,BLACK, (0,0,width,SQUARESIZE))
                posx = event.pos[0]
                posy = event.pos[1]
                draw_board(board)
                if turn == 0:
                    #screen.blit(Red_Circle,(posx,posy))
                    pygame.draw.circle(screen,BLACK,(posx, posy),RADIUS)
                else:
                    pygame.draw.circle(screen,WHITE,(posx, posy),RADIUS)
                
            pygame.display.update()
           
                #print (event.pos)
            if state == 0:
                    if turn == 0:
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                           posx = event.pos[0]
                           posy = event.pos[1]
                           col = int(math.floor(posx/SQUARESIZE)) 
                           row = int(posy/SQUARESIZE) - 1
                           print ("new input 1:")
                           print ("col:",col)
                           print ("row:",row)
                           if col < 3:
                                if row < 3:
                                        square = 0
                                else:
                                        row = row -3
                                        square = 1
                           else:
                                col = col -3
                                if row < 3:
                                        square = 2
                                else:
                                        row = row -3
                                        square = 3
                           print ("col:",col)
                           print ("row:",row)
                           print ("square:",square)
                
                           if is_valid_location(board, square ,col,row):
                                #row = get_next_open_row(board,col)
                                drop_piece(board,square,row,col,1)
                                print(board)
                                if winning_move(board, 1):
                                    print("Player 1 wins!")
                                    game_over = True
                           state = 1
                           draw_board(board)
                    else:
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            posx = event.pos[0]
                            posy = event.pos[1]
                            col = int(math.floor(posx/SQUARESIZE)) 
                            row = int(posy/SQUARESIZE) -1
                            print ("new input 2:")
                            print ("col:",col)
                            print ("row:",row)
                           
                            if col < 3:
                                if row < 3:
                                        square = 0
                                else:
                                        row = row -3
                                        square = 1
                            else:
                                col = col -3
                                if row < 3:
                                        square = 2
                                else:
                                        row = row -3
                                        square = 3
                            print ("col:",col)
                            print ("row:",row)
                            print ("square:",square)
                            if is_valid_location(board, square ,col,row):
                                #row = get_next_open_row(board,col)
                                drop_piece(board,square,row,col,2)
                                print (board)
                                if winning_move(board, 2):
                                    print("Player 2 wins!")
                                    game_over = True
                            state = 1    
                            draw_board(board)
            else:
                    if turn == 0:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                           posx = event.pos[0]
                           posy = event.pos[1]
                           col = int(math.floor(posx/SQUARESIZE)) 
                           row = int(posy/SQUARESIZE) - 1
                           if col < 3:
                                if row < 3:
                                        square = 0
                                else:
                                        row = row -3
                                        square = 1
                           else:
                                col = col -3
                                if row < 3:
                                        square = 2
                                else:
                                        row = row -3
                                        square = 3
                           if event.button == 1:
                                   rotate_a_square_counter_clockwise(board,square)
                           elif event.button == 3:
                                   rotate_a_square_clockwise(board,square)     
                           draw_board(board)
                           state = 0
                           turn = 1
                    else:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                           posx = event.pos[0]
                           posy = event.pos[1]
                           col = int(math.floor(posx/SQUARESIZE)) 
                           row = int(posy/SQUARESIZE) - 1
                           if col < 3:
                                if row < 3:
                                        square = 0
                                else:
                                        row = row -3
                                        square = 1
                           else:
                                col = col -3
                                if row < 3:
                                        square = 2
                                else:
                                        row = row -3
                                        square = 3
                           if event.button == 1:
                                   rotate_a_square_counter_clockwise(board,square)
                           elif event.button == 3:
                                   rotate_a_square_clockwise(board,square)
                           draw_board(board)
                           state = 0
                           turn = 0
            """if turn == 0:
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                           posx = event.pos[0]
                           posy = event.pos[1]
                           col = int(math.floor(posx/SQUARESIZE)) 
                           row = int(posy/SQUARESIZE) - 1
                           print ("new input 1:")
                           print ("col:",col)
                           print ("row:",row)
                           if col < 3:
                                if row < 3:
                                        square = 0
                                else:
                                        row = row -3
                                        square = 1
                           else:
                                col = col -3
                                if row < 3:
                                        square = 2
                                else:
                                        row = row -3
                                        square = 3
                           print ("col:",col)
                           print ("row:",row)
                           print ("square:",square)
                
                           if is_valid_location(board, square ,col,row):
                                #row = get_next_open_row(board,col)
                                drop_piece(board,square,row,col,1)
                                print(board)
                                if winning_move(board, 1):
                                    print("Player 1 wins!")
                                    game_over = True
                           turn += 1
                           draw_board(board)
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                           posx = event.pos[0]
                           posy = event.pos[1]
                           col = int(math.floor(posx/SQUARESIZE)) 
                           row = int(posy/SQUARESIZE) - 1
                           print ("new input 1:")
                           print ("col:",col)
                           print ("row:",row)
                           if col < 3:
                                if row < 3:
                                        square = 0
                                else:
                                        row = row -3
                                        square = 1
                           else:
                                col = col -3
                                if row < 3:
                                        square = 2
                                else:
                                        row = row -3
                                        square = 3
                           rotate_a_square(board,square)     
                           draw_board(board) 
                #input for player 2
            else:
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            posx = event.pos[0]
                            posy = event.pos[1]
                            col = int(math.floor(posx/SQUARESIZE)) 
                            row = int(posy/SQUARESIZE) -1
                            print ("new input 2:")
                            print ("col:",col)
                            print ("row:",row)
                           
                            if col < 3:
                                if row < 3:
                                        square = 0
                                else:
                                        row = row -3
                                        square = 1
                            else:
                                col = col -3
                                if row < 3:
                                        square = 2
                                else:
                                        row = row -3
                                        square = 3
                            print ("col:",col)
                            print ("row:",row)
                            print ("square:",square)
                            if is_valid_location(board, square ,col,row):
                                #row = get_next_open_row(board,col)
                                drop_piece(board,square,row,col,2)
                                print (board)
                                if winning_move(board, 2):
                                    print("Player 2 wins!")
                                    game_over = True
                            turn += 1
                            turn = turn % 2
                            draw_board(board)
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                           posx = event.pos[0]
                           posy = event.pos[1]
                           col = int(math.floor(posx/SQUARESIZE)) 
                           row = int(posy/SQUARESIZE) - 1
                           print ("new input 1:")
                           print ("col:",col)
                           print ("row:",row)
                           if col < 3:
                                if row < 3:
                                        square = 0
                                else:
                                        row = row -3
                                        square = 1
                           else:
                                col = col -3
                                if row < 3:
                                        square = 2
                                else:
                                        row = row -3
                                        square = 3
                           rotate_a_square(board,square)
                           draw_board(board)"""
