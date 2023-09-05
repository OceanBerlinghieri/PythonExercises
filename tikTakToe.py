import random
import time

PERSON = 1
COMPUTER = 0

#Print the matrix
def printBoard(board):
        for i in range(3):
            for j in range(3):
                print(board[i][j], end="   ")
            print("\n")

#Board is initialized with numbers from 1 to 9
def initBoard():
    board =  [[1+i+(j*3) for i in range(3)] for j in range(3)]
    board[1][1] = 'X'
    return board

#Computer generates random move
def moveComputer():
    moveRow = random.randint(0,2)
    moveColumn = random.randint(0,2)
                
    while board[moveRow][moveColumn] in ['X', 'O']:
        moveRow = random.randint(0,2)
        moveColumn = random.randint(0,2)
            
    board[moveRow][moveColumn] = 'X'

#User introduces row and column and call to check move function to validate move
def movePlayer():
    while True:
        #Block try except to avoid ValueError
        try:
            moveRow = int(input("Introduce your row: "))
            moveColumn = int(input("Introduce your column: "))
            break
        except ValueError:
            print("Not a valid move")
    #We check the option of row and column on 1 over 0, we want the user to reference the rows and columns above zero
    if checkMove(moveRow, moveColumn):
        board[moveRow-1][moveColumn-1] = 'O'
    else:
        movePlayer()

#Given a row and a column from a player, checks if move can be done and returns true if so
def checkMove(row, column):
    while(row < 1 or row > 3 or column < 1 or column > 3):
            print("Invalid input, try again")
            return False
        
    while board[row-1][column-1] in ['X', 'O']:
            print("Invalid input, try again")
            return False
    
    return True

#Check the function to see if can be modularized
def move(player):
    #Can be a independent function like moveComputer()
    if player == COMPUTER:
        moveComputer()
        time.sleep(random.randint(1,2))

    #Can be a independent function like movePerson()
    if player == PERSON:
        movePlayer()

def Draw(board):
    for i in range(3):
        for j in range(3):
            if board[j][i] in range(1,9):
                return False
    print("It's a draw")
    return True

def winHorizontals(board):
    if board[0][0] == board[0][1] == board[0][2] == 'O' or board[1][0] == board[1][1] == board[1][2] == 'O' or board[2][0] == board[2][1] == board[2][2] == 'O':
        print("Player wins")
        return True
    elif board[0][0] == board[0][1] == board[0][2] == 'X' or board[1][0] == board[1][1] == board[1][2] == 'X' or board[2][0] == board[2][1] == board[2][2] == 'X':
        print("Computer wins")
        return True
    
def winVerticals(board):
    if board[0][0] == board[1][0] == board[2][0] == 'O' or board[1][1] == board[2][1] == 'O' or board[0][2] == board[1][2] == board[2][2] == 'O':
        print("Player wins")
        return True    
    elif board[0][0] == board[1][0] == board[2][0] == 'X' or board[0][1] == board[1][1] == board[2][1] == 'X' or board[0][2] == board[1][2] == board[2][2] == 'X':
        print("Computer wins")
        return True

def winDiagonals(board):
    if board[0][0] == board[1][1] == board[2][2] == 'O' or board[0][2] == board[1][1] == board[2][0] == 'O':
        print("Player wins")
        return True
    elif board[0][0] == board[1][1] == board[2][2] == 'X' or board[0][2] == board[1][1] == board[2][0] == 'X':
        print("Computer wins")
        return True
    
#Check every win option or if board is full and its a draw
def win(board):
    return winHorizontals(board) or winVerticals(board) or winDiagonals(board) or Draw(board)
              
while True:
    if input("Do you want to start? Introduce N if you want to exit: ").upper() == 'N':
        break
    else:
        board = initBoard()
        player = PERSON

        while not win(board):
            printBoard(board)
            move(player)
            
            if player == PERSON:
                player = COMPUTER
                print("Board after player turn")
            else:
                player = PERSON
                print("Board after computer turn")
        
        printBoard(board)


