from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 1):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l != r:
                if nums[l] + nums[r] + nums[i] == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                elif nums[l] + nums[r] + nums[i] < 0:
                    l += 1
                else:
                    r -= 1

        return result


# test
nums = [-1, 0, 1, 2, -1, -4]  # [[-1,-1,2],[-1,0,1]]
nums_1 = []  # []
nums_2 = [0]  # []

Ex = Solution()
print(Ex.threeSum(nums_1))
