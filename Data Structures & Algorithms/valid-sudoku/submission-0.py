class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = [[[] for _ in range(3)] for _ in range(3)]

        for i in range(len(board)):
            row_arr = []
            column_arr = []

            for j in range(len(board)):

                if board[i][j] != ".":
                    row_arr += board[i][j]
                    squares[i//3][j//3] += board[i][j]

                if board[j][i] != ".":
                    column_arr += board[j][i]


            if len(row_arr) != len(set(row_arr)) or len(column_arr) != len(set(column_arr)):
                return False

        for i in squares:
            for j in i:
                if len(j) != len(set(j)):
                    return False

        return True
