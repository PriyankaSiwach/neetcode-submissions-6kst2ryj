class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows,cols= len(obstacleGrid), len(obstacleGrid[0])
        row=[0]*cols
        row[cols-1]=1
        for i in range(rows-1,-1,-1):
            for j in range(cols-1,-1,-1):
                if obstacleGrid[i][j]==1:
                    row[j]=0
                else:
                    if j+1<cols:
                        row[j]=row[j+1]+row[j]
        return row[0]

