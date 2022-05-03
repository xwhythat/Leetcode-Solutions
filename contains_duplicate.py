class Solution:
    def containsDuplicate(self, nums) -> bool:
        set_nums = set(nums)
        if len(set_nums) < len(nums):
            return True
        return False


# test
nums1 = [1, 2, 3, 1]
nums2 = [1, 2, 3, 4]
nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

A = Solution()
print(A.containsDuplicate(nums3))