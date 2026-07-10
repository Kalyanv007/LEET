class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        box=[set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                box_no=(i//3)*3 +(j//3)
                if board[i][j]==".":
                    continue
                if board[i][j] not in box[box_no] and board[i][j] not in rows[i] and board[i][j] not in cols[j]:
                    box[box_no].add(board[i][j])
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                else:
                    return False
        return True