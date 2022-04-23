class Solution:
    """"
    1. Проверка наличия соседа. Если он есть, вернуть его координаты
    2. Если его нет, вернуться в предыдущую итерацию
    """

    def maxAreaOfIsland(self, grid) -> int:
        height = len(grid)
        width = len(grid[0])
        status = [[False for j in range(width)] for i in range(height)]

        def neighbourPos(grid, i, j):
            if i > 0 and grid[i - 1][j] == 1 and status[i - 1][j] == False: # upper neighbour
                return i - 1, j
            elif j < width - 1 and grid[i][j + 1] == 1 and status[i][j + 1] == False: # right neighbour
                return i, j + 1
            elif i < height - 1 and grid[i + 1][j] == 1 and status[i + 1][j] == False: # bottom neighbour
                return i + 1, j
            elif j > 0 and grid[i][j - 1] == 1 and status[i][j - 1] == False: # left neighbour
                return i, j - 1
            else:
                return False

        def islandArea(grid, status, i, j, s=1):
            status[i][j] = True
            while neighbourPos(grid, i, j):
                x, y = neighbourPos(grid, i, j)
                s = islandArea(grid, status, x, y, s + 1)

            return s
        max_area = 0
        for i in range(height):
            for j in range(width):
                if not status[i][j] and grid[i][j] == 1:
                    area = islandArea(grid, status, i, j)
                    if area > max_area:
                        max_area = area

        return max_area

grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

grid2 = [[0,0,0,0,0,0,0,0]]
A = Solution()
print(A.maxAreaOfIsland(grid2))