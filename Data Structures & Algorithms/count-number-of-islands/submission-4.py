class Solution:
    def numIslands(self, board: List[List[str]]) -> int:
        rows, cols= len(board), len(board[0])

        def dfs(r,c):
            if r<0 or c<0 or r==rows or c ==cols or board[r][c]=="0":
                return
            else:
                board[r][c]="0"
                dfs(r+1, c)
                dfs(r-1,c)
                dfs(r, c+1)
                dfs(r, c-1)
        islands=0
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="1":
                    dfs(r,c)
                    islands+=1
        return islands
            