"""
Link: https://leetcode.com/problems/n-queens/
"""


def isSafe(board, row, column, n):
    # check if a queen is already placed in the current row and already visited columns
    for j in range(0, column):
        if (board[row][j] == 'Q'):
            return False

        # check if a queen is already placed in the left upper diagonal of the current (row,col)
    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if board[i][j] == 'Q':
            return False

        # check if a queen is already placed in the left lower diagonal of the current (row,col)
    for i, j in zip(range(row, n), range(column, -1, -1)):
        if board[i][j] == 'Q':
            return False

        # No need to check right diagonals as the right columns are not yet visited.

    return True


def helper(n, board, col, output):
    # if all columns are visited then we got a solution.
    if col == n:
        output.append(["".join(i) for i in board])
        return

    # For a given column, Iterate through all the rows to place the queen
    for i in range(n):
        if isSafe(board, i, col, n):  # check if it is safe to place the queen
            board[i][col] = 'Q'
            helper(n, board, col + 1, output)  # after placing the queen at current column, move to next column
            board[i][col] = '.'  # remove the placed queen to explore other possibilities

    return


def solveNQueens(n: int):
    board = [['.' for j in range(n)] for i in range(n)]

    output = []

    helper(n, board, 0, output)

    return output


def test_cases():
    list_of_cases = [
        {
            "s": 4,
            "o": [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
        },
        {
            "s": 1,
            "o": [["Q"]]
        },
    ]
    for case in range(len(list_of_cases)):
        output = solveNQueens(list_of_cases[case]["s"])
        result = (output == list_of_cases[case]["o"])
        print("#", case, result)
        if not result:
            print("Expected Output", list_of_cases[case]["o"])
            print("Actual Output", output)


test_cases()