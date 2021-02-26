# this is my sudoku solver program

# The zeroes will represent empty positions
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

board2 = [
    [6, 0, 5, 7, 0, 0, 1, 3, 2],
    [7, 0, 0, 6, 0, 0, 5, 0, 8],
    [0, 1, 9, 3, 0, 0, 0, 0, 4],
    [0, 2, 0, 0, 0, 3, 0, 0, 0],
    [0, 7, 3, 9, 0, 0, 2, 5, 0],
    [0, 5, 1, 2, 0, 0, 0, 0, 9],
    [5, 0, 8, 0, 0, 0, 0, 2, 0],
    [0, 4, 0, 0, 7, 6, 9, 1, 5],
    [0, 9, 0, 0, 4, 0, 6, 8, 0]
]

# recursive function
# remember the backtracking algorithm, we will not make it to the end of the board unless eveyrthing we put is correct
# Because if something is wrong, that means we would've backtracked to the last possible descrepency and choose a different "path" or number option
def solve(bo):

    # this will be our base case because if there are no more empty squares, then the board is solved
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
    
    # here, we are now checking to see which number we will choose
    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            # we run the recursive step right after we add in a value.
            # So this is how we go through the board (calling solve again with our new board)
            if solve(bo):
                return True # could this also be a continue statment?

            # this is the backtracking element that will set the position back to 0 if none of the numbers workeds
            # could we put this in an else statment?
            bo[row][col] = 0

    return False


# We have to check if the number is valid for that position. We can do so by checking its current 3x3 and its row and cols
def valid(bo, num, pos):
    # check row
    for i in range(len(bo)):
        # Because we are checking if the num that we just placed is valid or not, we will not check the poisition that we just placed the number into
        # That is what the second part of the if statement is for. 
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # check which 3x3 the num is in
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    # this is because let's say we are checking position (0, 3) in our game.
    # 0//3 == 0 would put us in the top 3 rows of the board, and 3//3 == 1 would put us in the midde 3 columns of the board
    # so, we are thinking of it as the top row to bottom would be 0, 1, 2, and left to right would be 0, 1, 2

    # this part will check the 3x3 that the num is in!
    for i in range(box_y * 3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            # again, we are not checking the same position that we just added the num to
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

# print out any board to visualize
def print_board(bo):
    for i in range(len(bo)):
        # if row is multiple of 3, print out a horizontal line but don't do it at the start (just looks cleaner)
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            # if column is multiple of 3, draw the vertical line but don't do it at the 0 (just looks cleaner)
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
                # the end="" means to ignore \n

            # when we reach the last number in a row, print it along with its \n
            if j == 8:
                print(bo[i][j])
            # this will print out all of the other numbers without the \n
            else:
                print(str(bo[i][j]) + " ", end="")

# Find an empty square to start with
def find_empty(bo):
    # checks through the rows
    for i in range(len(bo)):
        # checks through the columns
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                # return a tuple when we found our empty spot
                return (i, j)  # row, col

    return None

# print the original board
print_board(board2)
# solve the original board
solve(board2)
print("__________________________") # this line is just to separate the original from the finished
# print the finished board
print_board(board2)

