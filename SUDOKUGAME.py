
def printBoard(board):
    for i in range(len(board)):
        if i!=0 and i%3== 0:
            print("- - - - - - - - - - - - - - - - ")

        for j in range(len(board)):
            if j!=0 and j%3 ==0:
                print(" | ", end = "")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j])+" ", end = " ")
def checkBoard(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]==0:
                return i, j
    return None
def Valide(board, row, col, num):
    # check row
    for i in range(len(board)):
        if board[row][i]==num:
            return False
    #check col
    for i in range(len(board)):
        if board[i][col]== num:
            return False
    #check 3x3
    y0 = row//3
    x0 = col//3
    for i in range(y0*3, y0*3+3):
        for j in range(x0*3, x0*3+3):
            if board[i][j]== num:
                return False
    return True
def solveResult(board):
    if not checkBoard(board):
        return True
    else:
        row, col = checkBoard(board)
    for i in range(1, 10):
        if Valide(board, row, col, i):
            board[row][col]=i
            if solveResult(board):
                return True
            #backtrakin
            board[row][col]=0
    return False

grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
print("original board:")
printBoard(grid)
solveResult(grid)
print("Solution board:")
printBoard(grid)



