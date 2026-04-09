class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=collections.defaultdict(set)
        cols=collections.defaultdict(set)
        sqaures=collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                index= board[r][c]
                if index==".":
                    continue
                if (index in rows[r] or index in cols[c] or index in sqaures[(r//3, c//3)]):
                    return False
                rows[r].add(index)
                cols[c].add(index)
                sqaures[(r//3, c//3)].add(index)
        return True

        