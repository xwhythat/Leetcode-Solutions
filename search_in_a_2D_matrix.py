# https://leetcode.com/problems/search-a-2d-matrix/
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) * len(matrix[0]) - 1
        m = len(matrix[0])

        while l <= r:
            mid = l + (r - l) // 2

            if matrix[mid // m][mid % m] < target:
                l = mid + 1
            elif matrix[mid // m][mid % m] > target:
                r = mid - 1
            else:
                return True

        return False


# test
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
matrix1 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target1 = 13

Ex = Solution()
print(Ex.searchMatrix(matrix1, target1))
