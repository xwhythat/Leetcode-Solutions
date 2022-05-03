class Solution:
    def twoSum(self, nums, target):
        indices = []
        for i in range(len(nums)):
            indices.append((nums[i], i))

        nums.sort()

        l = 0
        r = len(nums) - 1

        while nums[l] + nums[r] != target:
            if nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1

        first = -1
        second = -1

        for i in range(len(indices)):
            if nums[l] == indices[i][0] and first == -1:
                first = indices[i][1]
            elif nums[r] == indices[i][0] and second == -1:
                second = indices[i][1]

        return [first, second]

# test
nums1 = [2, 7, 11, 15]
target1 = 9

nums2 = [3, 2, 4] # sorted(nums) = [2,3,4], indices = [(3,0), (2,1), (4,2)]
target2 = 6

nums3 = [3, 3]
target3 = 6

Example = Solution()
print(Example.twoSum(nums2, target2))
