class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        rows, cols = len(board), len(board[0])
        next_board = [[0] * cols for _ in range(rows)]

        def get_live_neighbors(row, col):
            live_neighbors = 0
            for r in range(max(row-1, 0), min(row+2, rows)):
                for c in range(max(col-1, 0), min(col+2, cols)):
                    if r == row and c == col:
                        continue
                    if board[r][c] == 1:
                        live_neighbors += 1
            return live_neighbors

        for r in range(rows):
            for c in range(cols):
                live_neighbors = get_live_neighbors(r, c)
                if board[r][c] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        next_board[r][c] = 0
                    else:
                        next_board[r][c] = 1
                else:
                    if live_neighbors == 3:
                        next_board[r][c] = 1

        # update the board with the next state
        for r in range(rows):
            for c in range(cols):
                board[r][c] = next_board[r][c]
