import numpy as np
import pygame 
import sys

pygame.init()

SQUARESIZE = 90 * 3
squarescreen = 90 * 8
COL = 6
ROW = 6
state_pass = 0
indsqu = 90

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
DARK_RED = (169,0,0)
WHITE = (255,255,255)

radius = int(indsqu/2 - 5)

squares = 4
rows = 3 
columns = 3 

turn = 0
state = 0
game_over = False

board = np.zeros((squares, rows, columns))

size = (squarescreen, squarescreen)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Pentago")


running = True


def check_range(value):
    if value > 70 and value < 150:
        x = 1
    elif value > 160 and value < 238:
        x = 2
    elif value > 249 and value < 329:
        x = 3
    elif value > 386 and value < 463:
        x = 4
    elif value > 476 and value < 554:
        x = 5
    elif value > 566 and value < 644:
        x = 6
    else: x = 0
    
    return x

def check_quad(x, y):
    row = check_range(x)
    col = check_range(y)
    
    if (row == 1 or row ==2  or row==3 ) and (col ==1 or col==2 or col ==3):
        quad = 0
    elif (row == 1 or row ==2  or row==3 ) and (col ==4 or col==5 or col ==6):
        quad = 2
    elif (row == 4 or row ==5  or row==6 ) and (col ==1 or col==2 or col ==3):
        quad = 1
    elif (row == 4 or row ==5  or row==6 ) and (col ==4 or col==5 or col ==6):
        quad = 3
    else:
        return -1
    return quad
    
    


def draw_board(screen, board):
    
    pygame.draw.rect(screen, RED, (65,65,SQUARESIZE, SQUARESIZE), 2)
    for c in range(3):
        for r in range(3):
            pygame.draw.rect(screen,RED, ((c*indsqu)+65, (r*indsqu)+65, indsqu, indsqu))
            
            if board[0][r][c] == 0:
                pygame.draw.circle(screen,DARK_RED, (int(c*indsqu+(indsqu/2))+65, int(r*indsqu+(indsqu/2))+65), radius)
            if board[0][r][c] == 1:
                pygame.draw.circle(screen,WHITE, (int(c*indsqu+(indsqu/2))+65, int(r*indsqu+(indsqu/2))+65), radius)
            if board[0][r][c] == 2:
                pygame.draw.circle(screen,BLACK, (int(c*indsqu+(indsqu/2))+65, int(r*indsqu+(indsqu/2))+65), radius)


    pygame.draw.rect(screen, RED, (SQUARESIZE + 110, 65, SQUARESIZE, SQUARESIZE), 2)
    for c in range(3):
        for r in range(3):
            pygame.draw.rect(screen,RED, ((c*indsqu)+110 + SQUARESIZE, (r*indsqu)+65, indsqu, indsqu))
            
            if board[1][r][c] == 0:
                pygame.draw.circle(screen,DARK_RED, (int(c*indsqu+(indsqu/2))+380, int(r*indsqu+(indsqu/2))+65), radius)
            if board[1][r][c] == 1:
                pygame.draw.circle(screen,WHITE, (int(c*indsqu+(indsqu/2))+380, int(r*indsqu+(indsqu/2))+65), radius)
            if board[1][r][c] == 2:
                pygame.draw.circle(screen,BLACK, (int(c*indsqu+(indsqu/2))+380, int(r*indsqu+(indsqu/2))+65), radius)

    pygame.draw.rect(screen, RED, (65, 110 + SQUARESIZE, SQUARESIZE, SQUARESIZE), 2)
    for c in range(3):
        for r in range(3):
            pygame.draw.rect(screen,RED, ((c*indsqu)+65, (r*indsqu)+110 + SQUARESIZE, indsqu, indsqu))
            
            if board[2][r][c] == 0:
                pygame.draw.circle(screen,DARK_RED, (int(c*indsqu+(indsqu/2))+65, int(r*indsqu+(indsqu/2))+380), radius)
            if board[2][r][c] == 1:
                pygame.draw.circle(screen,WHITE, (int(c*indsqu+(indsqu/2))+65, int(r*indsqu+(indsqu/2))+380), radius)
            if board[2][r][c] == 2:
                pygame.draw.circle(screen,BLACK, (int(c*indsqu+(indsqu/2))+65, int(r*indsqu+(indsqu/2))+380), radius)

    pygame.draw.rect(screen, RED, (SQUARESIZE + 110, 110 + SQUARESIZE, SQUARESIZE, SQUARESIZE), 2)
    for c in range(3):
        for r in range(3):
            pygame.draw.rect(screen,RED, ((c*indsqu)+110 +SQUARESIZE, (r*indsqu)+110 + SQUARESIZE, indsqu, indsqu))
            
            if board[3][r][c] == 0:
                pygame.draw.circle(screen,DARK_RED, (int(c*indsqu+(indsqu/2))+380, int(r*indsqu+(indsqu/2))+380), radius)
            if board[3][r][c] == 1:
                pygame.draw.circle(screen,WHITE, (int(c*indsqu+(indsqu/2))+380, int(r*indsqu+(indsqu/2))+380), radius)
            if board[3][r][c] == 2:
                pygame.draw.circle(screen,BLACK, (int(c*indsqu+(indsqu/2))+380, int(r*indsqu+(indsqu/2))+380), radius)

def drop_piece(row, col, board, turn, piece):
    game_over = False

    if row > 3 and col > 3:
        quad = 3
        row = row - 4
        col = col - 4
    elif col > 3:
        quad = 1
        col = col - 4
        row = row - 1
    elif row > 3:
        quad = 2
        col = col - 1
        row = row - 4
    else:
        quad = 0
        row = row - 1
        col = col - 1
        
    if turn ==0:
        piece = 1
    else:
        piece = 2
        

    
    if not valid_move(row, col, quad):
        print("Space is already occupied, select another place")
        return turn, game_over
    else:
        turn += 1
        turn = turn % 2
        board[quad][row][col] = piece
        
        if winning_move(board, piece):
            game_over = True
            print(f'Congrats Player {piece}, you have won the game!')

        return turn, game_over


def valid_move(row, col, quad):
    global state_pass
    if board[quad][row][col] == 0:
        state_pass = 1
        return True
    else:
        state_pass = 0
        return False

def rotate_quad(board, quad, rotation, piece):
    left = 1
    right = 0
    game_over = False
    
    if rotation == left:
        board[quad] = list(zip(*reversed(board[quad])))
        board[quad] = list(zip(*reversed(board[quad])))
        board[quad] = list(zip(*reversed(board[quad])))
    elif rotation == right:
        board[quad] = list(zip(*reversed(board[quad])))
        
    if winning_move(board, piece):
        game_over = True
        print(f'Congrats Player {piece}, you have won the game!')
        
    return board, game_over

def winning_move(board, piece):
    #horizontal wins
    for i in range(len(board[0]) * 2):
        quad = 0
        row = i
        if i > 2:
            row = i - 3
        col = 0
        if i > 2:
            quad = 2
        if board[quad][row][col] == piece and board[quad][row][col+1] == piece and board[quad][row][col+2] == piece and board[quad + 1][row][col] == piece and board[quad+1][row][col+1] == piece:
            return True
        elif board[quad][row][col+1] == piece and board[quad][row][col+2] == piece and board[quad+1][row][col] == piece and board[quad + 1][row][col+1] == piece and board[quad+1][row][col+2] == piece:
            return True

            #vertical win
    for j in range(len(board[0]) * 2):
        quad = 0
        row = 0
        col = j
        if i > 2:
            col = j - 3
        if j > 2:
            quad = 1
        if board[quad][row][col] == piece and board[quad][row+1][col] == piece and board[quad][row+2][col] == piece and board[quad + 2][row][col] == piece and board[quad+2][row+1][col] == piece:
            return True
        elif board[quad][row+1][col] == piece and board[quad][row+2][col] == piece and board[quad+2][row][col] == piece and board[quad + 2][row+1][col] == piece and board[quad+2][row+2][col] == piece:
            return True
        #diagonal wins

    #middle diagonals
    if board[0][0][0] == piece and board[0][1][1] == piece and board[0][2][2] == piece and board[3][0][0] == piece and board[3][1][1] == piece:
        return True
    if board[0][1][1] == piece and board[0][2][2] == piece and board[3][0][0] == piece and board[3][1][1] == piece and board[3][2][2] == piece:
        return True
    if board[2][2][0] == piece and board[2][1][1] == piece and board[2][0][2] == piece and board[1][2][0] == piece and board[1][1][1] == piece:
        return True
    if board[2][1][1] == piece and board[2][0][2] == piece and board[1][2][0] == piece and board[1][1][1] == piece and board[1][0][2] == piece:
        return True
    #side diagonals
    if board[0][1][0] == piece and board[0][2][1] == piece and board[2][0][2]== piece and board[3][1][0] == piece and board[3][2][1] == piece:
        return True
    if board[0][0][1] == piece and board[0][1][2] == piece and board[1][2][0]== piece and board[3][0][1] == piece and board[3][1][2] == piece:
        return True
    if board[1][0][1] == piece and board[1][1][0] == piece and board[0][2][2]== piece and board[2][0][1] == piece and board[2][1][0] == piece:
        return True
    if board[1][1][2] == piece and board[1][2][1] == piece and board[3][0][0]== piece and board[2][1][2] == piece and board[2][2][1] == piece:
        return True
    return False          

def clear_board(board):
    board = np.zeros((squares, rows, columns))

    return board
            
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            running = False
        if state == 0:
            if event.type == pygame.MOUSEBUTTONDOWN:
               
                x = event.pos[0]
                y = event.pos[1]
                    
                col = check_range(x)
                row = check_range(y)
                if col == 0 or row == 0:
                    continue
                else:
                    if turn == 0:
                        piece = 1
                        new, game_over = drop_piece(row, col, board, turn, piece)
                    else:
                        piece = 2
                        new, game_over = drop_piece(row, col, board, turn, piece)
                        
                turn = new  
                if game_over == True:
                    #button with message that game is over and ask if want to play again
                    board = clear_board(board)
                    draw_board(screen, board)
                    pygame.display.update()
                if  state_pass == 1:
                    print ("Hey")
                    state += 1
                else:
                    state = 0;
                    
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = event.pos[0]
                y = event.pos[1]
                
                quad = check_quad(x, y)
                print(f'Quad: {quad}')
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    rotation = 1
                    print(f'Rotation: {rotation}')
                if event.key == pygame.K_RIGHT:
                    rotation = 0
                    print(f'Rotation: {rotation}')
                
                        
                board, game_over = rotate_quad(board, quad, rotation, piece)
                
                
                state += 1
                state = state % 2
        
        
        draw_board(screen, board)
        pygame.display.update()
        
                
            
            
            
            
            
            
            
            
            
            
            
            
