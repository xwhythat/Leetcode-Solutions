from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxL = height[l]
        maxR = height[r]
        water = 0

        while l < r:
            if height[l] <= height[r]:
                l += 1
                if height[l] > maxL:
                    maxL = height[l]
                else:
                    water += maxL - height[l]

            else:
                r -= 1
                if height[r] > maxR:
                    maxR = height[r]
                else:
                    water += maxR - height[r]

        return water


# test
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]  # 6
height_2 = [4, 2, 0, 3, 2, 5]  # 9
height_3 = [4, 2, 3]  # 1
height_4 = [1]

Ex = Solution()
print(Ex.trap(height_4))