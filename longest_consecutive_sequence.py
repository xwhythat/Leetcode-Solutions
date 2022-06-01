from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in setNums:
                length = 0
                while num + length in setNums:
                    length += 1
                longest = max(length, longest)

        return longest



        return max_chain

# test
nums = [100, 4, 200, 1, 3, 2]  #4
nums2 = [0,3,7,2,5,8,4,6,0,1]  #9
nums3 = [9,1,-3,2,4,8,3,-1,6,-2,-4,7]
nums4 = [0,3,7,2,5,8,4,6,0,1]

Ex = Solution()
print(Ex.longestConsecutive(nums3))

print(sorted([0,3,7,2,5,8,4,6,0,1]))