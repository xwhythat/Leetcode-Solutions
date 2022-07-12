from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r)//2
            if nums[mid] > target:
                r = mid
            elif nums[mid] < target:
                l = mid
            else:
                return mid

            if r - l < 1:
                if nums[l] == target:
                    return l
                elif nums[r] == target:
                    return r
                else:
                    return -1


# test
nums = [-1, 0, 3, 5, 9, 12]
target = 9
nums2 = [-1, 0, 3, 5, 9, 12]
target2 = 2
nums3 = [-1,0,3,5,9,12]

Ex = Solution()
print(Ex.search(nums3, target2))
