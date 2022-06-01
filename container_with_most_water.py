# https://leetcode.com/problems/container-with-most-water/
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        def countArea(l, r):
            return (r - l) * min(height[l], height[r])

        max_area = 0
        l = 0
        r = len(height) - 1

        while l < r:
            curr_area = countArea(l, r)
            if curr_area > max_area:
                max_area = curr_area

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area


# test
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]  # 49
height_2 = [1, 1]  # 1

Ex = Solution()
print(Ex.maxArea(height_2))