from typing import List
import numpy as np

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums)

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result


nums = [1, 2, 3, 4]  # [24, 12, 8, 6]
nums_2 = [-1, 1, 0, -3, 3]  # [0, 0, 9, 0, 0]

Ex = Solution()
print(Ex.productExceptSelf(nums))