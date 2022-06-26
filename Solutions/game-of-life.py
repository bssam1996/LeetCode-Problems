"""
Link: https://leetcode.com/problems/game-of-life/
"""


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        alternative_board = [[board[j][i] for i in range(len(board[0]))] for j in range(len(board))]
        num_rows = len(alternative_board)
        num_columns = len(alternative_board[0])
        for row in range(len(alternative_board)):
            for column in range(len(alternative_board[0])):
                current_value = alternative_board[row][column]
                total_sum = 0
                # Above Rows
                if row > 0:
                    total_sum += sum(alternative_board[row - 1][max(column - 1, 0):min(column + 2, num_columns)])
                # Below Rows
                if row < num_rows - 1:
                    total_sum += sum(alternative_board[row + 1][max(column - 1, 0):min(column + 2, num_columns)])
                # Left Column
                if column > 0:
                    total_sum += alternative_board[row][column - 1]
                # Left Column
                if column < num_columns - 1:
                    total_sum += alternative_board[row][column + 1]
                if total_sum > 3 or total_sum < 2:
                    board[row][column] = 0
                elif total_sum == 3:
                    board[row][column] = 1

