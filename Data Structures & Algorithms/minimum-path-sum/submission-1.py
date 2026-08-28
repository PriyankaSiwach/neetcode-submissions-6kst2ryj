class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        row = [float("inf")] * (cols + 1)
        row[cols - 1] = 0

        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                row[c] = grid[r][c] + min(row[c], row[c + 1])

        return row[0]
